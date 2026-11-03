# Foton report

Status: **passed**

```json
{
  "scene": "teaching_reflectance70",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_reflectance70",
    "category": "teaching",
    "question": "How much does 0.7 surface reflectance add at the back of the room?",
    "interactions": [
      "multiple_bounces",
      "reflectance",
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
    "shades": 0,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "c3a99403ffdfb13ca5a865404aecdfab1d592c4fa3d780ab7cfaac12e2a2501d",
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
      "scene_fingerprint": 18345719022415901050,
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
      "scene_fingerprint": 18345719022415901050,
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
    "model_sha256": "604bce1ee9039eb5453e17b9f49feda721ce1a628c0bae6531660592d3375aa4",
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
          "maximum": 0.00029224716126918793,
          "p95": 1.1893303599208524e-05,
          "p99": 0.00012718886137008667
        },
        "bias_percent": -0.060910624560303654,
        "identifier": "teaching_reflectance70_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.9651389221795657,
        "worst_index": [
          17,
          121,
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
          "maximum": 0.0015379451215267181,
          "p95": 8.796649053692813e-05,
          "p99": 0.00021190382540225983
        },
        "bias_percent": 0.6946299636919449,
        "identifier": "teaching_reflectance70_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.1760801640416128,
        "worst_index": [
          6,
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
          "maximum": 0.0007215738296508789,
          "p95": 7.050720159895709e-05,
          "p99": 0.00015116645954549313
        },
        "bias_percent": 0.09801608069033574,
        "identifier": "teaching_reflectance70_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.640737921056344,
        "worst_index": [
          26,
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005513099022209644,
                  "p50": 0.0,
                  "p90": 3.9103906601667404e-07,
                  "p95": 9.427499753655862e-05,
                  "p99": 0.0002631478710100055
                },
                "candidate_energy": 8.943492510949,
                "cvrmse_percent": 8.923553026152716,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.12132239310811903,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.954356150117746,
                "relative_energy_error_percent": 0.12132239310811904,
                "rms_normalized_rmse_percent": 2.2038878819411867,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.013624615035951138,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.014175924938172102,
                  "rgb_channel": 0,
                  "sky_patch_index": 73
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0012515559792518616,
                  "p50": 0.0,
                  "p90": 4.819964669877663e-05,
                  "p95": 0.00019091013600700503,
                  "p99": 0.0004921408835798502
                },
                "candidate_energy": 4.362049160458724,
                "cvrmse_percent": 34.784533565055995,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.30887566186024273,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 4.3486173398684365,
                "relative_energy_error_percent": 0.3088756618602427,
                "rms_normalized_rmse_percent": 2.511444965187458,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.033882465213537216,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.03513402119278908,
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 109.84820895828307,
            "full": 224.45966699160635
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 112.46333306189626,
            "full": 227.25741704925895
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 111.28941609058529,
            "full": 227.49966592527926
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 124.31404204107821,
            "full": 227.814708952792
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00046371109783649445,
                  "p50": 0.0,
                  "p90": 2.641390892677009e-06,
                  "p95": 9.025360341183815e-05,
                  "p99": 0.0002051745541393757
                },
                "candidate_energy": 8.94613846910579,
                "cvrmse_percent": 6.997836048284667,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.07178837859231386,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.95256537062778,
                "relative_energy_error_percent": 0.07178837859231386,
                "rms_normalized_rmse_percent": 1.7280889708335678,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.006269202334806323,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.0067329134326428175,
                  "rgb_channel": 0,
                  "sky_patch_index": 50
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.001289360225200653,
                  "p50": 6.960037524095242e-07,
                  "p90": 7.769765215925872e-05,
                  "p95": 0.0001461968655348755,
                  "p99": 0.00037642777897417545
                },
                "candidate_energy": 11.786696492099061,
                "cvrmse_percent": 10.996951897683006,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0769185972234917,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.777637298702828,
                "relative_energy_error_percent": 0.0769185972234917,
                "rms_normalized_rmse_percent": 1.3312979478570082,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.06931160390377045,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.0706009641289711,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.80754199717194,
            "full": 2370.4582089558244
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 148.62391690257937,
            "full": 2408.1960420589894
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 152.10712503176183,
            "full": 2356.0292499605566
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 145.02162509597838,
            "full": 2381.4779580570757
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00026814243756234646,
                  "p50": 0.0,
                  "p90": 4.620524123311043e-07,
                  "p95": 6.780706025892865e-05,
                  "p99": 0.0001861469354480505
                },
                "candidate_energy": 8.951251837364907,
                "cvrmse_percent": 5.839228911137505,
                "energy_difference_negligible": false,
                "nmbe_percent": -0.07630572417595408,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.958087370805515,
                "relative_energy_error_percent": 0.07630572417595408,
                "rms_normalized_rmse_percent": 1.441984189167368,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.004414801485836506,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.004146659048274159,
                  "rgb_channel": 0,
                  "sky_patch_index": 75
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0011698491871356964,
                  "p50": 6.968828074604971e-07,
                  "p90": 7.901737990323454e-05,
                  "p95": 0.0001394732302287593,
                  "p99": 0.0003318884992040694
                },
                "candidate_energy": 11.931277395981162,
                "cvrmse_percent": 9.876096287207178,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.17498525876028448,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.910435888921455,
                "relative_energy_error_percent": 0.17498525876028448,
                "rms_normalized_rmse_percent": 1.2003847205925793,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07027706503868103,
                  "global_sensor_index": 33,
                  "local_sensor_index": 33,
                  "reference": 0.06910721585154533,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 142.0335000148043,
            "full": 2659.6489580115303
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.33212506305426,
            "full": 2709.56954092253
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 137.98837503418326,
            "full": 2687.371625099331
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 146.37500001117587,
            "full": 2699.022833025083
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
            "identifier": "teaching_reflectance70_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002733368892222643,
                  "p50": 0.0,
                  "p90": 6.260816007852554e-07,
                  "p95": 4.469323321245611e-05,
                  "p99": 0.0001112041063606739
                },
                "candidate_energy": 8.952624063839266,
                "cvrmse_percent": 3.9406066622122844,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.05401218106855746,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.947791166672687,
                "relative_energy_error_percent": 0.05401218106855746,
                "rms_normalized_rmse_percent": 0.9729992830311294,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007270418107509613,
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "reference": 0.007543754996731877,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0008350126445293427,
                  "p50": 5.442409047873298e-07,
                  "p90": 5.219777813181281e-05,
                  "p95": 9.100559764192429e-05,
                  "p99": 0.00021997292060405016
                },
                "candidate_energy": 11.94240809350876,
                "cvrmse_percent": 6.64075003126341,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.0564381316034478,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 11.949151971624001,
                "relative_energy_error_percent": 0.056438131603447794,
                "rms_normalized_rmse_percent": 0.8084837013346261,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.07070708647370338,
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "reference": 0.06987207382917404,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 208.94208399113268,
            "full": 5185.486707952805
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 210.7430830365047,
            "full": 5242.960750008933
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.95150003302842,
            "full": 5216.7970419395715
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 206.33812493178993,
            "full": 5222.184125101194
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
    "/private/tmp/claude-501/-Users-ssanjay-GitHub-foton/8946f656-9403-4636-9221-f1de0ea23053/scratchpad/main-wt/validation/results/2026-11-03-architectural-v4-metal-0.3.0-release/teaching_reflectance70/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 764.2454169690609,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance70/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2669.479166972451,
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
        "identifier": "teaching_reflectance70_grid",
        "full_identifier": "teaching_reflectance70_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05723220978688256,
            "cvrmse_percent": 2.4774779687458786,
            "rms_normalized_rmse_percent": 0.6117136004025637,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272297551739,
            "relative_energy_error_percent": 0.05723220978688257,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.248906720429523e-06,
              "p99": 6.368057802319527e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -2.1172028674369656,
            "cvrmse_percent": 21.701873509190662,
            "rms_normalized_rmse_percent": 2.6409479542653256,
            "reference_energy": 11.942591089364887,
            "candidate_energy": 11.689742208374582,
            "relative_energy_error_percent": 2.117202867436965,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.292591489094775e-06,
              "p90": 9.447659249417484e-05,
              "p95": 0.0001368492550682276,
              "p99": 0.0002604518085718155,
              "maximum": 0.0034363269805908203
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08257922530174255,
              "candidate": 0.07914289832115173,
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
            "nmbe_percent": -1.2345581000642687,
            "cvrmse_percent": 12.392744630286657,
            "rms_normalized_rmse_percent": 2.638726964124491,
            "reference_energy": 20.89598761359843,
            "candidate_energy": 20.63801450592632,
            "relative_energy_error_percent": 1.2345581000642771,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.2408376025850885e-06,
              "p90": 9.320362005382776e-05,
              "p95": 0.00013601365935755888,
              "p99": 0.00025957863545045257,
              "maximum": 0.0034363269805908203
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.08257922530174255,
              "candidate": 0.07914289832115173,
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
        "identifier": "teaching_reflectance70_grid",
        "full_identifier": "teaching_reflectance70_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.05723220978688256,
            "cvrmse_percent": 2.4774779687458786,
            "rms_normalized_rmse_percent": 0.6117136004025637,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272297551739,
            "relative_energy_error_percent": 0.05723220978688257,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.248906720429523e-06,
              "p99": 6.368057802319527e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 17,
              "local_sensor_index": 17,
              "sky_patch_index": 135,
              "rgb_channel": 0,
              "reference": 0.0017829914577305317,
              "candidate": 0.0015408495673909783,
              "position": [
                2.5,
                0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 168.6765217829377,
            "cvrmse_percent": 957.4182166644886,
            "rms_normalized_rmse_percent": 69.21002368857978,
            "reference_energy": 4.350861076658816,
            "candidate_energy": 11.689742208374582,
            "relative_energy_error_percent": 168.6765217829377,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0008906094881240278,
              "p95": 0.0011197925916349048,
              "p99": 0.0016742496518418193,
              "maximum": 0.03470359556376934
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026353744789958,
              "candidate": 0.06105734035372734,
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
            "nmbe_percent": 55.123383243436805,
            "cvrmse_percent": 313.0920869478413,
            "rms_normalized_rmse_percent": 69.20776616145561,
            "reference_energy": 13.304257600892356,
            "candidate_energy": 20.63801450592632,
            "relative_energy_error_percent": 55.12338324343681,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0008898099767975509,
              "p95": 0.0011264956730883558,
              "p99": 0.0016747518675401807,
              "maximum": 0.03470359556376934
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026353744789958,
              "candidate": 0.06105734035372734,
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
      "bias_percent": -0.6007338513845049,
      "rms_normalized_error_percent": 0.5603854369997804,
      "absolute_error": {
        "p95": 0.3320757378818482,
        "p99": 0.33701261831064283,
        "maximum": 0.3387686237241354
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 22.53044318453265,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.5603854369997804
    },
    "overcast": {
      "bias_percent": -0.5532336463606472,
      "rms_normalized_error_percent": 0.4882863691014716,
      "absolute_error": {
        "p95": 0.20572876930236816,
        "p99": 0.21175312995910645,
        "maximum": 0.21204185485839844
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 14.194230079650879,
      "reference_fraction_of_uniform": 0.6300022602081299,
      "rms_normalized_to_uniform_percent": 0.3338464926043201
    },
    "horizon": {
      "bias_percent": -1.1925598091251657,
      "rms_normalized_error_percent": 2.466889290467531,
      "absolute_error": {
        "p95": 0.11860424013893295,
        "p99": 0.12111890222395101,
        "maximum": 0.12135539169120468
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.4896849074795138,
      "reference_fraction_of_uniform": 0.11050314843290364,
      "rms_normalized_to_uniform_percent": 0.2015482750289166
    },
    "north": {
      "bias_percent": -20.693762875826085,
      "rms_normalized_error_percent": 127.15302733868883,
      "absolute_error": {
        "p95": 0.0001882381411633105,
        "p99": 0.0002599339137304922,
        "maximum": 0.0002968481567222625
      },
      "worst_index": [
        20
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 5.685944051947445e-05,
      "reference_fraction_of_uniform": 2.5236715828214074e-06,
      "rms_normalized_to_uniform_percent": 0.00031746104902021383
    },
    "east": {
      "bias_percent": -0.6750580244638916,
      "rms_normalized_error_percent": 0.6960831029193316,
      "absolute_error": {
        "p95": 0.0958518385887146,
        "p99": 0.12087901830673217,
        "maximum": 0.12299680709838867
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.644670486450195,
      "reference_fraction_of_uniform": 0.2061508744955063,
      "rms_normalized_to_uniform_percent": 0.15804622981660515
    },
    "south": {
      "bias_percent": -0.5679308202465208,
      "rms_normalized_error_percent": 0.6063015124460835,
      "absolute_error": {
        "p95": 0.2184913158416748,
        "p99": 0.23773660659790036,
        "maximum": 0.24590301513671875
      },
      "worst_index": [
        29
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.623618125915527,
      "reference_fraction_of_uniform": 0.6934447884559631,
      "rms_normalized_to_uniform_percent": 0.39491594627298715
    },
    "west": {
      "bias_percent": -0.6933421124429505,
      "rms_normalized_error_percent": 0.6750980553906482,
      "absolute_error": {
        "p95": 0.0765468180179596,
        "p99": 0.0887674033641815,
        "maximum": 0.09303665161132812
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.473663330078125,
      "reference_fraction_of_uniform": 0.19856081902980804,
      "rms_normalized_to_uniform_percent": 0.14688723383989621
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
        "identifier": "teaching_reflectance70_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.5965959974021272,
          "cvrmse_percent": 2.110423174445942,
          "absolute_error_percentiles_lux": {
            "p50": 8.669586181640625,
            "p90": 65.82134399414066,
            "p95": 94.71857910156245,
            "p99": 163.4434313964843
          },
          "maximum_absolute_error_lux": 441.15625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 6914.10693359375,
            "radiance_lux": 7355.26318359375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.16242009132420027,
            "maximum_error_percentage_points": 0.5739726027397296,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09365981135980977,
            "maximum_error_percentage_points": 0.26088556479103886,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07305555555555553,
            "maximum_error_percentage_points": 0.29958904109589213,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.19071156773211564,
            "maximum_error_percentage_points": 1.1734246575342553,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.2048173515981736,
            "maximum_error_percentage_points": 1.2850684931506855,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
      "maximum_error_percentage_points": 0.004975385273965571,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004975385273965571,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_reflectance70_grid",
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
      "study_preparation_seconds": 0.006470709107816219,
      "weather_seconds": 0.09541804203763604,
      "metric_reduction_seconds": 0.037354083033278584,
      "write_seconds": 0.03742412501014769,
      "total_seconds": 0.1703568750526756,
      "cold_end_to_end_seconds": 0.17682758416049182,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.011319208075292408,
      "engine_upload_seconds": 0.00027079200000000006,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.01898337504826486,
      "engine_annual_reduction_seconds": 0.00044008332770317793,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.01898337504826486
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006470709107816219,
      "weather_seconds": 0.09073487494606525,
      "metric_reduction_seconds": 0.011526582995429635,
      "write_seconds": 0.026254791067913175,
      "total_seconds": 0.12865620804950595,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.12865620804950595,
      "raw_export_seconds": 0.009615624905563891,
      "engine_upload_seconds": 6.0333e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00035308324731886387,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.01402033306658268,
      "full": 0.02518008300103247
    }
  },
  "elapsed_seconds": 0.6890204170485958,
  "result_class": "passed"
}
```
