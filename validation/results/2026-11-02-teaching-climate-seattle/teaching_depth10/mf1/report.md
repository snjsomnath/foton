# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth10",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth10",
    "category": "teaching",
    "question": "How does daylight fall off in a 10 m deep room?",
    "interactions": [
      "multiple_bounces",
      "room",
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
    "sensors": 60,
    "floor_area": 60.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "9cb5ba0ebe6272f2c0d54d5173dcdaab1278bc57b1c09e6ce155be20e6beda9e",
  "weather_sha256": "67ef83472f8207a15e51875aa6e0f8ccf8b790e4fa9c78142c709d765ff48de1",
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
      "scene_fingerprint": 2060527330165905083,
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
      "scene_fingerprint": 2060527330165905083,
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
        "identifier": "teaching_depth10_grid",
        "bias_percent": -0.053493837857983485,
        "rms_normalized_error_percent": 0.975898300851194,
        "absolute_error": {
          "p95": 1.8997874576598185e-06,
          "p99": 7.131975144147873e-05,
          "maximum": 0.00029224716126918793
        },
        "worst_index": [
          29,
          121,
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
        "identifier": "teaching_depth10_grid",
        "bias_percent": 0.04232051453612809,
        "rms_normalized_error_percent": 1.073743133561933,
        "absolute_error": {
          "p95": 4.168734012637282e-05,
          "p99": 0.00014557549729943275,
          "maximum": 0.0008203387260437012
        },
        "worst_index": [
          28,
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
        "identifier": "teaching_depth10_grid",
        "bias_percent": 0.0796427715919081,
        "rms_normalized_error_percent": 0.9083537298536877,
        "absolute_error": {
          "p95": 3.2993487548083056e-05,
          "p99": 0.00011110305786132812,
          "maximum": 0.0007517673075199127
        },
        "worst_index": [
          28,
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
            "identifier": "teaching_depth10_grid",
            "start_sensor_index": 0,
            "sensor_count": 60,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04320702189774483,
                "cvrmse_percent": 12.51855029095679,
                "rms_normalized_rmse_percent": 2.4616511656552285,
                "reference_energy": 9.23103668306976,
                "candidate_energy": 9.235025139110803,
                "relative_energy_error_percent": 0.04320702189774483,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.729498396045528e-05,
                  "p99": 0.0002346000401303172,
                  "maximum": 0.0006557726301252842
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.007664156146347523,
                  "candidate": 0.0070083835162222385
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.014652657475684186,
                "cvrmse_percent": 67.77431066607703,
                "rms_normalized_rmse_percent": 3.6000962723007772,
                "reference_energy": 3.4000362031903855,
                "candidate_energy": 3.3995380075314827,
                "relative_energy_error_percent": 0.014652657475684186,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.4806718172622132e-05,
                  "p95": 0.00012589883408509195,
                  "p99": 0.0004458990879356861,
                  "maximum": 0.0018442664295434952
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03574088588356972,
                  "candidate": 0.03389661945402622
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
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 108.41616697143763,
            "full": 305.23595795966685
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 113.33920795004815,
            "full": 302.77012498117983
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 113.90112491790205,
            "full": 302.9156250413507
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 115.37062504794449,
            "full": 293.4314579470083
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
            "identifier": "teaching_depth10_grid",
            "start_sensor_index": 0,
            "sensor_count": 60,
            "stages": {
              "direct": {
                "nmbe_percent": -0.01869872993020622,
                "cvrmse_percent": 9.019677395010406,
                "rms_normalized_rmse_percent": 1.7747074105715892,
                "reference_energy": 9.240708268124763,
                "candidate_energy": 9.238980373042068,
                "relative_energy_error_percent": 0.01869872993020622,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.4673919910565e-05,
                  "p99": 0.00017053750343620777,
                  "maximum": 0.0004227649769745767
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 39,
                  "sky_patch_index": 16,
                  "rgb_channel": 0,
                  "reference": 0.0023964779684320092,
                  "candidate": 0.0019737129914574325
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.32560843318618304,
                "cvrmse_percent": 22.065185750446805,
                "rms_normalized_rmse_percent": 1.8144564208605027,
                "reference_energy": 6.192866146363645,
                "candidate_energy": 6.213030640792137,
                "relative_energy_error_percent": 0.32560843318618304,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.7813711394865095e-07,
                  "p90": 2.7182354824617508e-05,
                  "p95": 8.120284182950822e-05,
                  "p99": 0.00027497089467942715,
                  "maximum": 0.0008588135242462158
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04177906550467014,
                  "candidate": 0.04263787902891636
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
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 160.55233299266547,
            "full": 3666.088083991781
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 156.36991593055427,
            "full": 3687.675041030161
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.18879200983793,
            "full": 3684.0206250781193
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 161.04645805899054,
            "full": 3669.1461249720305
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
            "identifier": "teaching_depth10_grid",
            "start_sensor_index": 0,
            "sensor_count": 60,
            "stages": {
              "direct": {
                "nmbe_percent": -0.06775185854614345,
                "cvrmse_percent": 8.537538804720109,
                "rms_normalized_rmse_percent": 1.680646971938926,
                "reference_energy": 9.244751208520029,
                "candidate_energy": 9.23848771775829,
                "relative_energy_error_percent": 0.06775185854614345,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.256280371919249e-05,
                  "p99": 0.00016041938215494156,
                  "maximum": 0.0005001146346330643
                },
                "worst": {
                  "global_sensor_index": 48,
                  "local_sensor_index": 48,
                  "sky_patch_index": 76,
                  "rgb_channel": 0,
                  "reference": 0.011453390121459961,
                  "candidate": 0.011953504756093025
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.03949597665308057,
                "cvrmse_percent": 21.410843022828434,
                "rms_normalized_rmse_percent": 1.7635184694690995,
                "reference_energy": 6.20648309392066,
                "candidate_energy": 6.208934405034412,
                "relative_energy_error_percent": 0.03949597665308058,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.833555600683212e-07,
                  "p90": 2.6829580747289678e-05,
                  "p95": 7.287924527190576e-05,
                  "p99": 0.00027675461024045944,
                  "maximum": 0.0007130096200853586
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 58,
                  "sky_patch_index": 49,
                  "rgb_channel": 0,
                  "reference": 0.00076515250839293,
                  "candidate": 5.214288830757141e-05
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
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.52766698319465,
            "full": 4013.6262910673395
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.68441699724644,
            "full": 4084.152749972418
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.0504590421915,
            "full": 4054.201708990149
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.5451659951359,
            "full": 3895.8921250887215
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
            "identifier": "teaching_depth10_grid",
            "start_sensor_index": 0,
            "sensor_count": 60,
            "stages": {
              "direct": {
                "nmbe_percent": 0.025217682484187726,
                "cvrmse_percent": 4.512208175749544,
                "rms_normalized_rmse_percent": 0.8878330343450744,
                "reference_energy": 9.238792690616265,
                "candidate_energy": 9.241122500022357,
                "relative_energy_error_percent": 0.025217682484187726,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3172353394329528e-05,
                  "p99": 8.568214252591133e-05,
                  "maximum": 0.0002154754474759102
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 94,
                  "rgb_channel": 0,
                  "reference": 0.013601639773696661,
                  "candidate": 0.013817115221172571
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.18891832487276808,
                "cvrmse_percent": 12.716798878807952,
                "rms_normalized_rmse_percent": 1.0483456493057262,
                "reference_energy": 6.227557362959818,
                "candidate_energy": 6.215792365909223,
                "relative_energy_error_percent": 0.18891832487276808,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4991235453010177e-07,
                  "p90": 1.819342687667825e-05,
                  "p95": 4.4125947169959464e-05,
                  "p99": 0.00015339022502303123,
                  "maximum": 0.00047911424189805984
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.028280514292418957,
                  "candidate": 0.027801400050520897
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
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 253.69375001173466,
            "full": 6944.524416932836
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 262.441165978089,
            "full": 6808.669041027315
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 245.15541701111943,
            "full": 6879.463625024073
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "60",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 244.30449993815273,
            "full": 6883.984417072497
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1899.0341669414192,
      "worker_pool_size": 12,
      "invocation_count": 4
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth10/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 7875.0692079775035,
      "worker_pool_size": 12,
      "invocation_count": 4
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      60,
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
        "identifier": "teaching_depth10_grid",
        "full_identifier": "teaching_depth10_grid",
        "start_sensor_index": 0,
        "sensor_count": 60,
        "stages": {
          "direct": {
            "nmbe_percent": -0.047490884835307945,
            "cvrmse_percent": 3.135704449168977,
            "rms_normalized_rmse_percent": 0.6172067070062369,
            "reference_energy": 9.243258315287335,
            "candidate_energy": 9.238868610125792,
            "relative_energy_error_percent": 0.047490884835307945,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.2330710887908936e-06,
              "p99": 4.893873665423598e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
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
            "nmbe_percent": -1.8943903070084396,
            "cvrmse_percent": 32.865330697182614,
            "rms_normalized_rmse_percent": 2.705981498952261,
            "reference_energy": 6.218374153205431,
            "candidate_energy": 6.1005738759935895,
            "relative_energy_error_percent": 1.8943903070084396,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.155510282544128e-07,
              "p90": 3.3394928323105025e-05,
              "p95": 5.30538371094735e-05,
              "p99": 0.00013733177911490202,
              "maximum": 0.001957762986421585
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.043193042278289795,
              "candidate": 0.04123527929186821,
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
            "nmbe_percent": -0.790278663151384,
            "cvrmse_percent": 13.182867000505004,
            "rms_normalized_rmse_percent": 2.6988278495267863,
            "reference_energy": 15.461632468492766,
            "candidate_energy": 15.339442486119381,
            "relative_energy_error_percent": 0.790278663151384,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.17395199292514e-07,
              "p90": 3.323334349261136e-05,
              "p95": 5.261941696517168e-05,
              "p99": 0.00012828758917748928,
              "maximum": 0.001957762986421585
            },
            "worst": {
              "global_sensor_index": 37,
              "local_sensor_index": 37,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.043193042278289795,
              "candidate": 0.04123527929186821,
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
      60,
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
        "identifier": "teaching_depth10_grid",
        "full_identifier": "teaching_depth10_grid",
        "start_sensor_index": 0,
        "sensor_count": 60,
        "stages": {
          "direct": {
            "nmbe_percent": -0.047490884835307945,
            "cvrmse_percent": 3.135704449168977,
            "rms_normalized_rmse_percent": 0.6172067070062369,
            "reference_energy": 9.243258315287335,
            "candidate_energy": 9.238868610125792,
            "relative_energy_error_percent": 0.047490884835307945,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.2330710887908936e-06,
              "p99": 4.893873665423598e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 29,
              "local_sensor_index": 29,
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
            "nmbe_percent": 79.98130888952556,
            "cvrmse_percent": 419.37170948833017,
            "rms_normalized_rmse_percent": 22.212799606441987,
            "reference_energy": 3.389559679076557,
            "candidate_energy": 6.1005738759935895,
            "relative_energy_error_percent": 79.98130888952556,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023204091703519234,
              "p95": 0.0003214275013306178,
              "p99": 0.0005875062197446823,
              "maximum": 0.010511541739106178
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017967429012060165,
              "candidate": 0.028478970751166344,
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
            "nmbe_percent": 21.4253422550934,
            "cvrmse_percent": 112.49938767047144,
            "rms_normalized_rmse_percent": 22.208093724542703,
            "reference_energy": 12.632817994363892,
            "candidate_energy": 15.339442486119381,
            "relative_energy_error_percent": 21.4253422550934,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00023258391029230553,
              "p95": 0.0003214824013411997,
              "p99": 0.0005751564167439938,
              "maximum": 0.010511541739106178
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017967429012060165,
              "candidate": 0.028478970751166344,
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
      "bias_percent": 0.05187025793358134,
      "rms_normalized_error_percent": 0.22034141918213537,
      "absolute_error": {
        "p95": 0.08447244557078276,
        "p99": 0.11095532334704783,
        "maximum": 0.123383845269748
      },
      "worst_index": [
        56
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 11.187528862912778,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.22034141918213537
    },
    "overcast": {
      "bias_percent": 0.05319114955094556,
      "rms_normalized_error_percent": 0.19089252339032117,
      "absolute_error": {
        "p95": 0.05768384933471679,
        "p99": 0.06286597490310666,
        "maximum": 0.06616616249084473
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.07841682434082,
      "reference_fraction_of_uniform": 0.6327060461044312,
      "rms_normalized_to_uniform_percent": 0.1334158235231682
    },
    "horizon": {
      "bias_percent": 0.6353881810785739,
      "rms_normalized_error_percent": 1.8583826613022898,
      "absolute_error": {
        "p95": 0.05507489077322319,
        "p99": 0.06226935184409485,
        "maximum": 0.06306889356884415
      },
      "worst_index": [
        56
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.166883940494647,
      "reference_fraction_of_uniform": 0.10430220603612707,
      "rms_normalized_to_uniform_percent": 0.11135837107664373
    },
    "north": {
      "bias_percent": -63.64240620139559,
      "rms_normalized_error_percent": 115.02679266325949,
      "absolute_error": {
        "p95": 8.230907515098805e-05,
        "p99": 0.00011028734260435147,
        "maximum": 0.0001287994091399014
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.5015446479083039e-05,
      "reference_fraction_of_uniform": 1.342159407613508e-06,
      "rms_normalized_to_uniform_percent": 0.00014228914994271336
    },
    "east": {
      "bias_percent": -0.12075954442512944,
      "rms_normalized_error_percent": 0.3089292388224588,
      "absolute_error": {
        "p95": 0.03286997079849242,
        "p99": 0.0353285527229309,
        "maximum": 0.03587841987609863
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.2511229515075684,
      "reference_fraction_of_uniform": 0.2012171745300293,
      "rms_normalized_to_uniform_percent": 0.07038199796446173
    },
    "south": {
      "bias_percent": 0.07381402671974663,
      "rms_normalized_error_percent": 0.2562767799704426,
      "absolute_error": {
        "p95": 0.07030618786811826,
        "p99": 0.08811634421348569,
        "maximum": 0.09440183639526367
      },
      "worst_index": [
        56
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.809897422790527,
      "reference_fraction_of_uniform": 0.698089599609375,
      "rms_normalized_to_uniform_percent": 0.1639236437928437
    },
    "west": {
      "bias_percent": 0.012284065131745497,
      "rms_normalized_error_percent": 0.33477978124923174,
      "absolute_error": {
        "p95": 0.03308678418397903,
        "p99": 0.04802630841732019,
        "maximum": 0.05900096893310547
      },
      "worst_index": [
        56
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.1701228618621826,
      "reference_fraction_of_uniform": 0.1939769685268402,
      "rms_normalized_to_uniform_percent": 0.07313074324252926
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
        "identifier": "teaching_depth10_grid",
        "sensor_count": 60,
        "illuminance": {
          "nmbe_percent": -0.09237694114179333,
          "cvrmse_percent": 1.659239362074726,
          "absolute_error_percentiles_lux": {
            "p50": 1.8221473693847656,
            "p90": 20.02052001953125,
            "p95": 32.258062744140624,
            "p99": 67.68584777832012
          },
          "maximum_absolute_error_lux": 282.33056640625,
          "worst": {
            "sensor_index": 58,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2414.5,
            "foton_lux": 5381.212890625,
            "radiance_lux": 5663.54345703125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.40816210045662077,
            "maximum_error_percentage_points": 1.7254794520547954,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.3316209052469031,
            "maximum_error_percentage_points": 1.456133690337623,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2702762557077626,
            "maximum_error_percentage_points": 1.3695890410958853,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2773652968036538,
            "maximum_error_percentage_points": 1.3695890410958853,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.015141552511415406,
            "maximum_error_percentage_points": 0.08260273972602761,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 43.333333333333336,
          "radiance_percent": 45.0,
          "difference_percentage_points": 1.6666666666666643,
          "tolerance_percentage_points": 2.0,
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
      "maximum_error_percentage_points": 0.004950502996578621,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_depth10_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth10_grid",
            "maximum_error_percentage_points": 0.004950502996578621,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth10_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth10_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth10_grid",
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
      "study_preparation_seconds": 0.0082394580822438,
      "weather_seconds": 0.09156941703986377,
      "metric_reduction_seconds": 0.05530866701155901,
      "write_seconds": 0.035303874989040196,
      "total_seconds": 0.18232195801101625,
      "cold_end_to_end_seconds": 0.19056141609326005,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.01806187501642853,
      "engine_upload_seconds": 0.00029949999999999996,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.036964791594073176,
      "engine_annual_reduction_seconds": 0.0004946249537169933,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.036964791594073176
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.0082394580822438,
      "weather_seconds": 0.08883091690950096,
      "metric_reduction_seconds": 0.011806917027570307,
      "write_seconds": 0.025893916958011687,
      "total_seconds": 0.12667220795992762,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.12667220795992762,
      "raw_export_seconds": 0.011876208009198308,
      "engine_upload_seconds": 6.05e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0005274582654237747,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.00768649997189641,
      "full": 0.029930250020697713
    }
  },
  "elapsed_seconds": 73.4812607500935,
  "result_class": "passed"
}
```
