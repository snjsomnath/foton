# Foton report

Status: **passed**

```json
{
  "scene": "offset_tower",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "offset_tower",
    "category": "context",
    "question": "Does an off-axis tall obstruction affect the appropriate sky sectors?",
    "interactions": [
      "closed_context",
      "asymmetric_obstruction",
      "height_contrast"
    ],
    "room_count": 1,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 1,
    "apertures": 1,
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "f061829fb9958279668d1a6b16ca66fc72cefe5e7b65609d941c7b925ded37ba",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 6801024155776306720,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 6801024155776306720,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
      "weather_id": "aff05f88fed2459a6796dca3cabd63daf743bc359ea5c7394adb01155f6785fb"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "fa596a1b71c81c8eee4f32b17ea6d10a57aabce8541ff637ac4a9c1ee69c4ac1"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
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
    "model_sha256": "36b3ac82d7687aaf37211b5cfd81d610b5cb7cd78d4769c55473ef131309ac0d",
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
          "maximum": 0.00044697802513837814,
          "p95": 1.6940757632255317e-06,
          "p99": 9.02470201253891e-05
        },
        "bias_percent": -0.0360559396541939,
        "identifier": "offset_tower_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0990600098957912,
        "worst_index": [
          23,
          132,
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
          "maximum": 0.0004984419792890549,
          "p95": 4.218512040097265e-05,
          "p99": 0.00012259278446435928
        },
        "bias_percent": 0.04283198179214833,
        "identifier": "offset_tower_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9920843338053906,
        "worst_index": [
          9,
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
          "maximum": 0.00036623142659664154,
          "p95": 3.4404914913466105e-05,
          "p99": 0.00011322298087179661
        },
        "bias_percent": 0.022050728423758544,
        "identifier": "offset_tower_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.8769237575389793,
        "worst_index": [
          7,
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0007064056117087603,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.055510555393902e-05,
                  "p99": 0.00027351523749530315
                },
                "candidate_energy": 5.341505613495428,
                "cvrmse_percent": 15.059885683885565,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.1958816990103936,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.351989180833698,
                "relative_energy_error_percent": 0.19588169901039362,
                "rms_normalized_rmse_percent": 2.89851560847762,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007268315646797419,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.007974721258506179,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008260856848210096,
                  "p50": 0.0,
                  "p90": 2.355192555114627e-05,
                  "p95": 0.0001053668148415451,
                  "p99": 0.0004266051109880209
                },
                "candidate_energy": 2.0738053533277565,
                "cvrmse_percent": 59.06699275709148,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.22187917114531389,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0692141980159775,
                "relative_energy_error_percent": 0.22187917114531389,
                "rms_normalized_rmse_percent": 3.376510615687732,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.0002838345244526863,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": -0.0005422511603683233,
                  "rgb_channel": 0,
                  "sky_patch_index": 46
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.72399999666959,
            "full": 221.03633300866932
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 105.28058302588761,
            "full": 225.0571249751374
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 102.09908301476389,
            "full": 233.37695805821568
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 118.82920807693154,
            "full": 221.0131249157712
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.90179193019867,
            "full": 251.03791698347777
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 120.72699994314462,
            "full": 222.8601659880951
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 110.58991600293666,
            "full": 221.8174160225317
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 107.59816691279411,
            "full": 229.45716592948884
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000418279436416924,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.385017309687096e-05,
                  "p99": 0.0002026660367846489
                },
                "candidate_energy": 5.334287926838442,
                "cvrmse_percent": 10.401383475198328,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.050039237206057206,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.336958500161927,
                "relative_energy_error_percent": 0.0500392372060572,
                "rms_normalized_rmse_percent": 1.999907554309255,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0033307180274277925,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0037489974638447165,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006335852667689323,
                  "p50": 9.823506843531504e-07,
                  "p90": 3.0011433409526944e-05,
                  "p95": 7.507908012485073e-05,
                  "p99": 0.00029347161762416363
                },
                "candidate_energy": 3.722300575357135,
                "cvrmse_percent": 22.524766385335006,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.20552563814794222,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7146659843876577,
                "relative_energy_error_percent": 0.20552563814794222,
                "rms_normalized_rmse_percent": 1.9578678080224645,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028962625190615654,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.029596210457384586,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 136.41591696068645,
            "full": 2208.578290999867
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.02699995599687,
            "full": 2233.440582989715
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.26466602645814,
            "full": 2236.2654999597
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 127.73854192346334,
            "full": 2273.256416898221
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003487849608063698,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.345754692214541e-05,
                  "p99": 0.0001408036332577467
                },
                "candidate_energy": 5.336947649188005,
                "cvrmse_percent": 7.846518601435569,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.03271677018351428,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.338694297532129,
                "relative_energy_error_percent": 0.03271677018351428,
                "rms_normalized_rmse_percent": 1.5084393503268436,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0034474364947527647,
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "reference": 0.0037962214555591345,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0007796352729201317,
                  "p50": 9.949934423048035e-07,
                  "p90": 2.953159491880797e-05,
                  "p95": 7.073711785778835e-05,
                  "p99": 0.0002725701779127121
                },
                "candidate_energy": 3.717981971324491,
                "cvrmse_percent": 21.939494343502595,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.11721597469684768,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7223451544788944,
                "relative_energy_error_percent": 0.11721597469684768,
                "rms_normalized_rmse_percent": 1.907525382274409,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.025555324740707874,
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "reference": 0.026334960013628006,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 134.46237496100366,
            "full": 2396.5381670277566
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 129.27516701165587,
            "full": 2352.2481250111014
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.1872500749305,
            "full": 2326.8978339619935
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 130.8211670257151,
            "full": 2412.887749960646
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
            "identifier": "offset_tower_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019422266632318497,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.217130386270576e-05,
                  "p99": 8.436013013124466e-05
                },
                "candidate_energy": 5.3378455864231,
                "cvrmse_percent": 4.647789814977854,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.04113694251680406,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 5.335650662877015,
                "relative_energy_error_percent": 0.04113694251680406,
                "rms_normalized_rmse_percent": 0.8933370477949661,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.010037424974143505,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.00984320230782032,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005701705813407898,
                  "p50": 7.32769498412722e-07,
                  "p90": 2.1029172785347328e-05,
                  "p95": 4.240716734784619e-05,
                  "p99": 0.00014730403199791908
                },
                "candidate_energy": 3.7230187358975257,
                "cvrmse_percent": 12.812299943714125,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.01154836809546229,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.723448733463112,
                "relative_energy_error_percent": 0.01154836809546229,
                "rms_normalized_rmse_percent": 1.115534557266341,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.029517030343413353,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.028946859762072563,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 186.64295901544392,
            "full": 4195.203459006734
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 190.2260830393061,
            "full": 4159.766749944538
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.48054205812514,
            "full": 4110.619416926056
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 181.80116696748883,
            "full": 4251.066791941412
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
    "/content/suite-vulkan-0.3.2/offset_tower/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 805.5924590444192,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/offset_tower/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2757.78337509837,
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
        "identifier": "offset_tower_grid",
        "full_identifier": "offset_tower_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.025847346954650123,
            "cvrmse_percent": 3.799920969938235,
            "rms_normalized_rmse_percent": 0.7304242318392201,
            "reference_energy": 5.3368748448529,
            "candidate_energy": 5.335495404295216,
            "relative_energy_error_percent": 0.025847346954650127,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.3928511179983578e-06,
              "p99": 5.1695387810468674e-05,
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
            "nmbe_percent": -1.1116329571842667,
            "cvrmse_percent": 24.97243465251199,
            "rms_normalized_rmse_percent": 2.1731216135495024,
            "reference_energy": 3.7231070366890204,
            "candidate_energy": 3.6817197518379388,
            "relative_energy_error_percent": 1.1116329571842665,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.4984275793494817e-06,
              "p90": 3.471667878329754e-05,
              "p95": 5.383534080465324e-05,
              "p99": 0.00014563929289579391,
              "maximum": 0.0013543646782636642
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025835145264863968,
              "candidate": 0.024480780586600304,
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
            "nmbe_percent": -0.4720398557959121,
            "cvrmse_percent": 10.181956567502361,
            "rms_normalized_rmse_percent": 2.156136210120965,
            "reference_energy": 9.05998188154192,
            "candidate_energy": 9.017215156133155,
            "relative_energy_error_percent": 0.4720398557959121,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.499302527463442e-06,
              "p90": 3.435382677707821e-05,
              "p95": 5.338600894901901e-05,
              "p99": 0.00013291672803461552,
              "maximum": 0.0013543646782636642
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025835145264863968,
              "candidate": 0.024480780586600304,
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
        "identifier": "offset_tower_grid",
        "full_identifier": "offset_tower_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.025847346954650123,
            "cvrmse_percent": 3.799920969938235,
            "rms_normalized_rmse_percent": 0.7304242318392201,
            "reference_energy": 5.3368748448529,
            "candidate_energy": 5.335495404295216,
            "relative_energy_error_percent": 0.025847346954650127,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.3928511179983578e-06,
              "p99": 5.1695387810468674e-05,
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
            "nmbe_percent": 76.88819969867401,
            "cvrmse_percent": 424.1631567966944,
            "rms_normalized_rmse_percent": 24.393395405086146,
            "reference_energy": 2.0813823409982604,
            "candidate_energy": 3.6817197518379388,
            "relative_energy_error_percent": 76.888199698674,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.9400000585155794e-06,
              "p90": 0.0002167999919038266,
              "p95": 0.00028642649413086464,
              "p99": 0.0004997848300263286,
              "maximum": 0.007586877793073654
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010575821623206139,
              "candidate": 0.018162699416279793,
              "position": [
                0.5,
                0.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.55436149250373,
            "cvrmse_percent": 119.00244846429231,
            "rms_normalized_rmse_percent": 24.391877505868912,
            "reference_energy": 7.418257185851161,
            "candidate_energy": 9.017215156133155,
            "relative_energy_error_percent": 21.554361492503734,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.9400000585155794e-06,
              "p90": 0.00021591433323919773,
              "p95": 0.0002912339143222197,
              "p99": 0.000508867553435266,
              "maximum": 0.007586877793073654
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.010575821623206139,
              "candidate": 0.018162699416279793,
              "position": [
                0.5,
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
      "bias_percent": 0.14708388390695934,
      "rms_normalized_error_percent": 0.28166129716970034,
      "absolute_error": {
        "p95": 0.11883690534284175,
        "p99": 0.13768990192177283,
        "maximum": 0.13800720254572996
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.794181041238197,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.28166129716970034
    },
    "overcast": {
      "bias_percent": 0.07004146839872133,
      "rms_normalized_error_percent": 0.23568193440890975,
      "absolute_error": {
        "p95": 0.06429433822631836,
        "p99": 0.08463426828384397,
        "maximum": 0.0901641845703125
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.902088642120361,
      "reference_fraction_of_uniform": 0.6394268274307251,
      "rms_normalized_to_uniform_percent": 0.16665071641674034
    },
    "horizon": {
      "bias_percent": 1.2603085504700273,
      "rms_normalized_error_percent": 2.7379977194165077,
      "absolute_error": {
        "p95": 0.07066997387657892,
        "p99": 0.08739670391807325,
        "maximum": 0.09626644845280041
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.01465534897729,
      "reference_fraction_of_uniform": 0.09400021595903299,
      "rms_normalized_to_uniform_percent": 0.15943273522818535
    },
    "north": {
      "bias_percent": -1.1539169151434019,
      "rms_normalized_error_percent": 3.1155548021773445,
      "absolute_error": {
        "p95": 0.004667274653911591,
        "p99": 0.0070604071021079995,
        "maximum": 0.007672101259231567
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": true,
      "reference_mean": 0.03002203442156315,
      "reference_fraction_of_uniform": 0.002781316637992859,
      "rms_normalized_to_uniform_percent": 0.010950404985687907
    },
    "east": {
      "bias_percent": 0.2485321632925355,
      "rms_normalized_error_percent": 0.41373483164254066,
      "absolute_error": {
        "p95": 0.020889893174171448,
        "p99": 0.026174065470695496,
        "maximum": 0.02619457244873047
      },
      "worst_index": [
        17
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.4723809957504272,
      "reference_fraction_of_uniform": 0.1364050656557083,
      "rms_normalized_to_uniform_percent": 0.05612178784216171
    },
    "south": {
      "bias_percent": 0.2294007354728133,
      "rms_normalized_error_percent": 0.35123114046777265,
      "absolute_error": {
        "p95": 0.10358840227127075,
        "p99": 0.12444612979888914,
        "maximum": 0.12832021713256836
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.702363967895508,
      "reference_fraction_of_uniform": 0.7135663032531738,
      "rms_normalized_to_uniform_percent": 0.23535360279745268
    },
    "west": {
      "bias_percent": -0.09360747965924243,
      "rms_normalized_error_percent": 0.30920205572222476,
      "absolute_error": {
        "p95": 0.025738820433616638,
        "p99": 0.02844356298446655,
        "maximum": 0.029672563076019287
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4718775749206543,
      "reference_fraction_of_uniform": 0.22900094091892242,
      "rms_normalized_to_uniform_percent": 0.07181851999671698
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
        "identifier": "offset_tower_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.02340547360822347,
          "cvrmse_percent": 1.8032311308612654,
          "absolute_error_percentiles_lux": {
            "p50": 2.1109466552734375,
            "p90": 22.98145751953125,
            "p95": 35.520373535156224,
            "p99": 69.43964355468727
          },
          "maximum_absolute_error_lux": 363.255859375,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5151.99267578125,
            "radiance_lux": 5515.24853515625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.46329908675799064,
            "maximum_error_percentage_points": 2.1619178082191794,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.19963011396878846,
            "maximum_error_percentage_points": 0.8832037868020848,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1112062404870625,
            "maximum_error_percentage_points": 0.4128767123287673,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11143074581430648,
            "maximum_error_percentage_points": 0.41424657534246023,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.022229832572298523,
            "maximum_error_percentage_points": 0.08410958904109478,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 47.22222222222222,
          "radiance_percent": 50.0,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
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
      "maximum_error_percentage_points": 0.004956656678089644,
      "metrics": {
        "da": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.004956656678089644,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "offset_tower_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "offset_tower_grid",
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
      "study_preparation_seconds": 0.47134464300006584,
      "weather_seconds": 0.2550603510003384,
      "metric_reduction_seconds": 0.15606430000025284,
      "write_seconds": 0.011693263000324805,
      "total_seconds": 0.4232284830000026,
      "cold_end_to_end_seconds": 0.8945731260000684,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0015201680002974172,
      "engine_upload_seconds": 0.014353303,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.011572742,
      "engine_annual_reduction_seconds": 0.005980943,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.011572742
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.47134464300006584,
      "weather_seconds": 0.22535599000002549,
      "metric_reduction_seconds": 0.15710884000009173,
      "write_seconds": 0.014005020999775297,
      "total_seconds": 0.39672494300020844,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.39672494300020844,
      "raw_export_seconds": 0.0016064229998846713,
      "engine_upload_seconds": 0.013971276,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.2e-08,
      "engine_annual_reduction_seconds": 0.006042041,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015257642000051419,
      "full": 0.02299768500006394
    }
  },
  "elapsed_seconds": 3.0314816990003237,
  "result_class": "passed"
}
```
