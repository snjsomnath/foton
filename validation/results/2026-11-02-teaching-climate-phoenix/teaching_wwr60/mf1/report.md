# Foton report

Status: **passed**

```json
{
  "scene": "teaching_wwr60",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_wwr60",
    "category": "teaching",
    "question": "How does a 60% window-to-wall ratio light the base room?",
    "interactions": [
      "multiple_bounces",
      "side_glazing",
      "window"
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
    "aperture_area": 10.799999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "f468516ac22b05619f3770702a9b0eea719f682029b3a66147a101614a239faf",
  "weather_sha256": "d6e21c48181f8f154e82514cc5fb46924d2844a9b5984ce6959d4ba6c95ddafe",
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
      "scene_fingerprint": 4824569144856164811,
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
      "scene_fingerprint": 4824569144856164811,
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_wwr60_grid",
        "bias_percent": 0.07397654505195622,
        "rms_normalized_error_percent": 1.0707843647350377,
        "absolute_error": {
          "p95": 3.569427644833896e-05,
          "p99": 0.0001636957749724388,
          "maximum": 0.0006659128703176975
        },
        "worst_index": [
          10,
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
        "identifier": "teaching_wwr60_grid",
        "bias_percent": 0.013445103571088659,
        "rms_normalized_error_percent": 0.6711207470715801,
        "absolute_error": {
          "p95": 0.00011353727895766496,
          "p99": 0.0002141227014362812,
          "maximum": 0.0006649717688560486
        },
        "worst_index": [
          19,
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
        "identifier": "teaching_wwr60_grid",
        "bias_percent": -0.007615429863734044,
        "rms_normalized_error_percent": 0.5105830578738962,
        "absolute_error": {
          "p95": 9.279006626456951e-05,
          "p99": 0.00017365813255310059,
          "maximum": 0.0005320236086845398
        },
        "worst_index": [
          19,
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
            "identifier": "teaching_wwr60_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.13765882725776715,
                "cvrmse_percent": 10.743476144601633,
                "rms_normalized_rmse_percent": 3.655760809360598,
                "reference_energy": 18.74865195316488,
                "candidate_energy": 18.774461127570248,
                "relative_energy_error_percent": 0.13765882725776715,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00018389802426099777,
                  "p95": 0.00035018659546039914,
                  "p99": 0.0005488600581884384,
                  "maximum": 0.001014817040413618
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 117,
                  "rgb_channel": 0,
                  "reference": 0.006574963219463825,
                  "candidate": 0.005560146179050207
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.9366545027687377,
                "cvrmse_percent": 37.374086777199125,
                "rms_normalized_rmse_percent": 2.9420804840688923,
                "reference_energy": 7.76720867256283,
                "candidate_energy": 7.694456762791827,
                "relative_energy_error_percent": 0.9366545027687377,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00026176124811172485,
                  "p95": 0.0004540100286249071,
                  "p99": 0.0008262395858764648,
                  "maximum": 0.0016146302223205566
                },
                "worst": {
                  "global_sensor_index": 4,
                  "local_sensor_index": 4,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.070796437561512,
                  "candidate": 0.06918180733919144
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 119.24550007097423,
            "full": 256.89854205120355
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.2105000205338,
            "full": 248.63516597542912
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 122.2729169530794,
            "full": 255.12483401689678
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 113.67229197639972,
            "full": 241.45204096566886
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
            "identifier": "teaching_wwr60_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.06866438278871637,
                "cvrmse_percent": 4.771661568640571,
                "rms_normalized_rmse_percent": 1.6251813718182484,
                "reference_energy": 18.764710020685015,
                "candidate_energy": 18.75182534836722,
                "relative_energy_error_percent": 0.06866438278871635,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.97653740644455e-05,
                  "p95": 0.000139632515492849,
                  "p99": 0.00026172446087002754,
                  "maximum": 0.0004700419376604259
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0018795249634422362,
                  "candidate": 0.002349566901102662
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.11409659837774212,
                "cvrmse_percent": 10.51232236691556,
                "rms_normalized_rmse_percent": 1.1144869605856011,
                "reference_energy": 12.981858374763828,
                "candidate_energy": 12.99667023357565,
                "relative_energy_error_percent": 0.11409659837774212,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 5.023798053116479e-07,
                  "p90": 0.00011271168477833271,
                  "p95": 0.0001996042497921734,
                  "p99": 0.0003866511397063732,
                  "maximum": 0.0009852945804595947
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.052502745762467384,
                  "candidate": 0.05348804034292698
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.09049997571856,
            "full": 2162.965999916196
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 184.8778340499848,
            "full": 2202.540291007608
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 173.6509168986231,
            "full": 2214.2994169844314
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 179.27645903546363,
            "full": 2183.875042013824
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
            "identifier": "teaching_wwr60_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.036553219822585616,
                "cvrmse_percent": 4.295576333940473,
                "rms_normalized_rmse_percent": 1.4639290635733007,
                "reference_energy": 18.756887966621434,
                "candidate_energy": 18.76374421311175,
                "relative_energy_error_percent": 0.03655321982258562,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.614997982978821e-05,
                  "p95": 0.0001341203518677503,
                  "p99": 0.00023615756072103977,
                  "maximum": 0.000364069826900959
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 120,
                  "rgb_channel": 0,
                  "reference": 0.01606075558811426,
                  "candidate": 0.01642482541501522
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.11342498465101222,
                "cvrmse_percent": 11.157325010885465,
                "rms_normalized_rmse_percent": 1.184420445900796,
                "reference_energy": 12.99885637858224,
                "candidate_energy": 12.984112427730025,
                "relative_energy_error_percent": 0.11342498465101221,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.82662699141656e-07,
                  "p90": 0.0001184293651022017,
                  "p95": 0.0002161766347853699,
                  "p99": 0.00040379539132118225,
                  "maximum": 0.0014245547354221344
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.09961242601275444,
                  "candidate": 0.0981878712773323
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 167.26474999450147,
            "full": 2293.746834038757
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 172.9429999832064,
            "full": 2269.3484579212964
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 163.35658403113484,
            "full": 2246.323375031352
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 167.73345903493464,
            "full": 2295.684834010899
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
            "identifier": "teaching_wwr60_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0032410396599548636,
                "cvrmse_percent": 2.3921036108113563,
                "rms_normalized_rmse_percent": 0.8148885036526655,
                "reference_energy": 18.758678383220285,
                "candidate_energy": 18.75928635942637,
                "relative_energy_error_percent": 0.003241039659954863,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.4781056456267834e-05,
                  "p95": 6.916355341672892e-05,
                  "p99": 0.00013221055269241333,
                  "maximum": 0.00026647094637155533
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 119,
                  "rgb_channel": 0,
                  "reference": 0.017578034661710262,
                  "candidate": 0.017844505608081818
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.05190057229748117,
                "cvrmse_percent": 6.104343873990648,
                "rms_normalized_rmse_percent": 0.6473080235615514,
                "reference_energy": 12.987029999357219,
                "candidate_energy": 12.99377034225133,
                "relative_energy_error_percent": 0.05190057229748117,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.7776685840308346e-07,
                  "p90": 6.265845149755478e-05,
                  "p95": 0.00011334483278915284,
                  "p99": 0.000216588843613863,
                  "maximum": 0.0006143525242805481
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.11065930128097534,
                  "candidate": 0.1100449487566948
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 238.86945797130466,
            "full": 3986.2130420515314
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 261.48483308497816,
            "full": 4000.536000006832
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 256.0770829441026,
            "full": 4007.2930000023916
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 251.06291705742478,
            "full": 3985.7069589197636
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 667.4878749763593,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_wwr60/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 2684.529999969527,
      "worker_pool_size": 12,
      "invocation_count": 3
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
        "identifier": "teaching_wwr60_grid",
        "full_identifier": "teaching_wwr60_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.019395785110179798,
            "cvrmse_percent": 1.6795928522472376,
            "rms_normalized_rmse_percent": 0.5720661368689874,
            "reference_energy": 18.762221318218508,
            "candidate_energy": 18.765860398347286,
            "relative_energy_error_percent": 0.019395785110179798,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.5739351511001587e-06,
              "p95": 2.1392607595771525e-05,
              "p99": 9.40435566008091e-05,
              "maximum": 0.0003807060420513153
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.006609765347093344,
              "candidate": 0.006229059305042028,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4344324380726776,
            "cvrmse_percent": 23.594021555563153,
            "rms_normalized_rmse_percent": 2.5024805130476158,
            "reference_energy": 12.987161184985617,
            "candidate_energy": 12.800869132163399,
            "relative_energy_error_percent": 1.4344324380726774,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.4701776649417297e-06,
              "p90": 6.919726729393005e-05,
              "p95": 0.000104298791848123,
              "p99": 0.00028396351262927055,
              "maximum": 0.0040706247091293335
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.11035212129354477,
              "candidate": 0.10628149658441544,
              "position": [
                3.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5752961421375878,
            "cvrmse_percent": 9.623257128535682,
            "rms_normalized_rmse_percent": 2.495237421283132,
            "reference_energy": 31.749382503204124,
            "candidate_energy": 31.566729530510685,
            "relative_energy_error_percent": 0.5752961421375877,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.4079759012020077e-06,
              "p90": 6.650760769844055e-05,
              "p95": 0.00010003386996686444,
              "p99": 0.0002556326799094677,
              "maximum": 0.0040706247091293335
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.11035212129354477,
              "candidate": 0.10628149658441544,
              "position": [
                3.5,
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
        "identifier": "teaching_wwr60_grid",
        "full_identifier": "teaching_wwr60_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": 0.019395785110179798,
            "cvrmse_percent": 1.6795928522472376,
            "rms_normalized_rmse_percent": 0.5720661368689874,
            "reference_energy": 18.762221318218508,
            "candidate_energy": 18.765860398347286,
            "relative_energy_error_percent": 0.019395785110179798,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.5739351511001587e-06,
              "p95": 2.1392607595771525e-05,
              "p99": 9.40435566008091e-05,
              "maximum": 0.0003807060420513153
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 119,
              "rgb_channel": 0,
              "reference": 0.006609765347093344,
              "candidate": 0.006229059305042028,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 65.59626260080853,
            "cvrmse_percent": 333.3443385098918,
            "rms_normalized_rmse_percent": 26.141283776350893,
            "reference_energy": 7.730167898185945,
            "candidate_energy": 12.800869132163399,
            "relative_energy_error_percent": 65.59626260080853,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 8.544417653411074e-07,
              "p90": 0.0006814665575802792,
              "p95": 0.0008804384036920963,
              "p99": 0.001413802383467555,
              "maximum": 0.022518664598464966
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06916108727455139,
              "candidate": 0.09167975187301636,
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
            "nmbe_percent": 19.153955019519834,
            "cvrmse_percent": 97.26817464241198,
            "rms_normalized_rmse_percent": 26.141878632883806,
            "reference_energy": 26.492389216404455,
            "candidate_energy": 31.566729530510685,
            "relative_energy_error_percent": 19.153955019519824,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 8.544417653411074e-07,
              "p90": 0.0006815572087361943,
              "p95": 0.000884634905378334,
              "p99": 0.0014185169711709023,
              "maximum": 0.022518664598464966
            },
            "worst": {
              "global_sensor_index": 34,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.06916108727455139,
              "candidate": 0.09167975187301636,
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
      "bias_percent": 0.1275316221802662,
      "rms_normalized_error_percent": 0.24485154230039405,
      "absolute_error": {
        "p95": 0.2298442890490211,
        "p99": 0.3144860027159989,
        "maximum": 0.3237085556593158
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 38.511831771680555,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.24485154230039405
    },
    "overcast": {
      "bias_percent": 0.10742609117483828,
      "rms_normalized_error_percent": 0.18762457293315554,
      "absolute_error": {
        "p95": 0.11935567855834961,
        "p99": 0.13664376735687256,
        "maximum": 0.13739728927612305
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 24.959871292114258,
      "reference_fraction_of_uniform": 0.6481091380119324,
      "rms_normalized_to_uniform_percent": 0.12960592334446136
    },
    "horizon": {
      "bias_percent": 1.1129917220148018,
      "rms_normalized_error_percent": 2.1260683255438324,
      "absolute_error": {
        "p95": 0.16867962218224308,
        "p99": 0.19978193010820763,
        "maximum": 0.2084261554404354
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.3581842143664513,
      "reference_fraction_of_uniform": 0.08719876619413029,
      "rms_normalized_to_uniform_percent": 0.14842206097917104
    },
    "north": {
      "bias_percent": 36.022890176501654,
      "rms_normalized_error_percent": 236.45632151415197,
      "absolute_error": {
        "p95": 0.00015974957614162122,
        "p99": 0.0004019302672531917,
        "maximum": 0.0005184857436688617
      },
      "worst_index": [
        35
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 3.4105967642972246e-05,
      "reference_fraction_of_uniform": 8.855971032062371e-07,
      "rms_normalized_to_uniform_percent": 0.00021049756622031104
    },
    "east": {
      "bias_percent": -0.027421790482909505,
      "rms_normalized_error_percent": 0.3533681824222237,
      "absolute_error": {
        "p95": 0.07159775495529175,
        "p99": 0.08523087501525876,
        "maximum": 0.09242630004882812
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.520109176635742,
      "reference_fraction_of_uniform": 0.19526749849319458,
      "rms_normalized_to_uniform_percent": 0.07625096672009551
    },
    "south": {
      "bias_percent": 0.1478606159091471,
      "rms_normalized_error_percent": 0.3307800020445367,
      "absolute_error": {
        "p95": 0.22727489471435547,
        "p99": 0.30088133811950674,
        "maximum": 0.3233461380004883
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 26.5345401763916,
      "reference_fraction_of_uniform": 0.6889970898628235,
      "rms_normalized_to_uniform_percent": 0.21214119884379978
    },
    "west": {
      "bias_percent": 0.0974446115556317,
      "rms_normalized_error_percent": 0.2936128108159298,
      "absolute_error": {
        "p95": 0.05149507522583008,
        "p99": 0.07506656646728511,
        "maximum": 0.08394527435302734
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.286218643188477,
      "reference_fraction_of_uniform": 0.18919427692890167,
      "rms_normalized_to_uniform_percent": 0.060813740614015004
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
        "identifier": "teaching_wwr60_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.05730987968187347,
          "cvrmse_percent": 0.9339789444777937,
          "absolute_error_percentiles_lux": {
            "p50": 11.3785400390625,
            "p90": 67.97666015625003,
            "p95": 96.01054687500005,
            "p99": 174.52321289062542
          },
          "maximum_absolute_error_lux": 538.390625,
          "worst": {
            "sensor_index": 4,
            "position": [
              0.5,
              1.5,
              0.75
            ],
            "hour_of_year": 7858.5,
            "foton_lux": 33506.78515625,
            "radiance_lux": 34045.17578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.02331811263317994,
            "maximum_error_percentage_points": 0.16808219178081174,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.012409788029619919,
            "maximum_error_percentage_points": 0.0502429630767125,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.012473363774733614,
            "maximum_error_percentage_points": 0.05753424657534234,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1465220700152211,
            "maximum_error_percentage_points": 0.520958904109591,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.14662480974124797,
            "maximum_error_percentage_points": 0.5484931506849313,
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
      "maximum_error_percentage_points": 0.004931506849317202,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_wwr60_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_wwr60_grid",
            "maximum_error_percentage_points": 0.004624357876707563,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_wwr60_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_wwr60_grid",
            "maximum_error_percentage_points": 0.004931506849314982,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_wwr60_grid",
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
      "study_preparation_seconds": 0.006904541980475187,
      "weather_seconds": 0.09603841707576066,
      "metric_reduction_seconds": 0.05347058305051178,
      "write_seconds": 0.028125374927185476,
      "total_seconds": 0.1777731670299545,
      "cold_end_to_end_seconds": 0.18467770901042968,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01762204198166728,
      "engine_upload_seconds": 0.000316125,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03373962489422411,
      "engine_annual_reduction_seconds": 0.0003370000049471855,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03373962489422411
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006904541980475187,
      "weather_seconds": 0.09270016697701067,
      "metric_reduction_seconds": 0.011987000005319715,
      "write_seconds": 0.01896370796021074,
      "total_seconds": 0.1238070409744978,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1238070409744978,
      "raw_export_seconds": 0.010127375018782914,
      "engine_upload_seconds": 5.6958e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0003550417022779584,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.008133915951475501,
      "full": 0.02132816705852747
    }
  },
  "elapsed_seconds": 42.38864633301273,
  "result_class": "passed"
}
```
