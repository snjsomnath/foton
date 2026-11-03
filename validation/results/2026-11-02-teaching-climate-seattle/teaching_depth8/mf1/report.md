# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth8",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth8",
    "category": "teaching",
    "question": "How does daylight fall off in an 8 m deep room?",
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
    "sensors": 48,
    "floor_area": 48.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "3716306930eabe611e26c30fe069ed6e3c95feab111b615e8352349ea79dac48",
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
      "scene_fingerprint": 7711455366643186943,
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
      "scene_fingerprint": 7711455366643186943,
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
        "identifier": "teaching_depth8_grid",
        "bias_percent": -0.05485834551319389,
        "rms_normalized_error_percent": 0.9725811534349869,
        "absolute_error": {
          "p95": 4.4424086809158325e-06,
          "p99": 9.02470201253891e-05,
          "maximum": 0.00029224716126918793
        },
        "worst_index": [
          23,
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
        "identifier": "teaching_depth8_grid",
        "bias_percent": 0.0513494323974199,
        "rms_normalized_error_percent": 0.9865110417523124,
        "absolute_error": {
          "p95": 5.423440597951412e-05,
          "p99": 0.00015830900520086288,
          "maximum": 0.000484611839056015
        },
        "worst_index": [
          45,
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
        "identifier": "teaching_depth8_grid",
        "bias_percent": 0.025696797494946903,
        "rms_normalized_error_percent": 0.8665879070386726,
        "absolute_error": {
          "p95": 4.3489970266819e-05,
          "p99": 0.00013526948168873787,
          "maximum": 0.0005291178822517395
        },
        "worst_index": [
          45,
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.012593163457955798,
                "cvrmse_percent": 11.256685006024256,
                "rms_normalized_rmse_percent": 2.45560180899985,
                "reference_energy": 9.147676140808471,
                "candidate_energy": 9.146524158999455,
                "relative_energy_error_percent": 0.012593163457955798,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 9.00698360055685e-05,
                  "p99": 0.0002369710709899664,
                  "maximum": 0.0006852950900793076
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 94,
                  "rgb_channel": 0,
                  "reference": 0.013340590056031942,
                  "candidate": 0.01402588514611125
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.46053586055042656,
                "cvrmse_percent": 52.175529680628486,
                "rms_normalized_rmse_percent": 2.98605733865643,
                "reference_energy": 3.2838985071958504,
                "candidate_energy": 3.2687749769461334,
                "relative_energy_error_percent": 0.46053586055042656,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.1729802620029688e-05,
                  "p95": 0.00015230634016916156,
                  "p99": 0.00042177014984190464,
                  "maximum": 0.0009367358579766005
                },
                "worst": {
                  "global_sensor_index": 42,
                  "local_sensor_index": 42,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": -0.00046772006317041814,
                  "candidate": 0.0004690157948061824
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 111.5788749884814,
            "full": 265.35445800982416
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.44929099362344,
            "full": 246.61145790014416
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 104.82599993702024,
            "full": 247.87399999331683
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 105.64112500287592,
            "full": 259.9200840340927
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04819081007154178,
                "cvrmse_percent": 8.380086180468389,
                "rms_normalized_rmse_percent": 1.8265100614734755,
                "reference_energy": 9.146922748675024,
                "candidate_energy": 9.14251477250582,
                "relative_energy_error_percent": 0.04819081007154179,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.16034958511591e-05,
                  "p99": 0.00018934346735477448,
                  "maximum": 0.0004918910562992096
                },
                "worst": {
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "sky_patch_index": 17,
                  "rgb_channel": 0,
                  "reference": 0.002785623073577881,
                  "candidate": 0.0022937320172786713
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.15093300862737716,
                "cvrmse_percent": 20.18682641180938,
                "rms_normalized_rmse_percent": 1.772977439648518,
                "reference_energy": 5.994981575277617,
                "candidate_energy": 6.00402998133584,
                "relative_energy_error_percent": 0.15093300862737713,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.1764321900263894e-07,
                  "p90": 3.3902710492839145e-05,
                  "p95": 9.317463263869286e-05,
                  "p99": 0.00030850968323647976,
                  "maximum": 0.0006415499374270439
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.026381785050034523,
                  "candidate": 0.027023334987461567
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 141.9034170685336,
            "full": 2980.760541977361
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.95595795474946,
            "full": 2998.5583340749145
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.91545895766467,
            "full": 2955.401916988194
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 136.65504101663828,
            "full": 2952.0563749829307
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.004041539550691244,
                "cvrmse_percent": 7.954261391690303,
                "rms_normalized_rmse_percent": 1.7325980259018943,
                "reference_energy": 9.142902448321365,
                "candidate_energy": 9.142532934302835,
                "relative_energy_error_percent": 0.004041539550691245,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.319896783679724e-05,
                  "p99": 0.00018381187692284584,
                  "maximum": 0.00041953311301767826
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.0038432865403592587,
                  "candidate": 0.0034237534273415804
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.15697932938442077,
                "cvrmse_percent": 21.03860115361075,
                "rms_normalized_rmse_percent": 1.8505381562939953,
                "reference_energy": 6.004570409156937,
                "candidate_energy": 6.013996343517647,
                "relative_energy_error_percent": 0.1569793293844208,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.2387551368296954e-07,
                  "p90": 3.5217498952988604e-05,
                  "p95": 0.00010644737631082535,
                  "p99": 0.00029453402385115623,
                  "maximum": 0.0009669605642557144
                },
                "worst": {
                  "global_sensor_index": 36,
                  "local_sensor_index": 36,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.032725075259804726,
                  "candidate": 0.03369203582406044
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.30716701503843,
            "full": 3160.974167054519
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.37387495208532,
            "full": 3214.2220420064405
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 153.47970800939947,
            "full": 3144.644416985102
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 142.2622089739889,
            "full": 3104.8425419721752
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
            "identifier": "teaching_depth8_grid",
            "start_sensor_index": 0,
            "sensor_count": 48,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0381408118266889,
                "cvrmse_percent": 4.551128443512256,
                "rms_normalized_rmse_percent": 0.9918706363268914,
                "reference_energy": 9.145393195466113,
                "candidate_energy": 9.14190506825662,
                "relative_energy_error_percent": 0.0381408118266889,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.169348929077387e-05,
                  "p99": 0.00011191517114639282,
                  "maximum": 0.00021255254978314042
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 43,
                  "sky_patch_index": 49,
                  "rgb_channel": 0,
                  "reference": 0.0017617855337448418,
                  "candidate": 0.0015492329839617014
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.15862868377769254,
                "cvrmse_percent": 12.186375091731538,
                "rms_normalized_rmse_percent": 1.0713258037531732,
                "reference_energy": 6.007480654428896,
                "candidate_energy": 6.017010241919216,
                "relative_energy_error_percent": 0.15862868377769254,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.7235421267969286e-07,
                  "p90": 2.201866009272639e-05,
                  "p95": 5.663000047206879e-05,
                  "p99": 0.0001736958511173725,
                  "maximum": 0.000682121142745018
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 37,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04070885479450226,
                  "candidate": 0.04002673365175724
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
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 225.94791708979756,
            "full": 5616.309333010577
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 223.8080829847604,
            "full": 5590.4661669628695
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 218.31833303440362,
            "full": 5630.016915965825
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "48",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 217.04608399886638,
            "full": 5537.839459022507
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 1254.3349580373615,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-seattle/teaching_depth8/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 4668.193040997721,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      48,
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
        "identifier": "teaching_depth8_grid",
        "full_identifier": "teaching_depth8_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04684107795519001,
            "cvrmse_percent": 2.821610071633558,
            "rms_normalized_rmse_percent": 0.6149477330048871,
            "reference_energy": 9.146421276938781,
            "candidate_energy": 9.14213699461834,
            "relative_energy_error_percent": 0.046841077955190005,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.8442591428756714e-06,
              "p99": 5.678832530975342e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
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
            "nmbe_percent": -1.4537938059766329,
            "cvrmse_percent": 28.50329970261626,
            "rms_normalized_rmse_percent": 2.5062629712258073,
            "reference_energy": 6.009473340028213,
            "candidate_energy": 5.922107988839066,
            "relative_energy_error_percent": 1.4537938059766327,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.592794138919999e-07,
              "p90": 3.756782971322545e-05,
              "p95": 6.07506517553702e-05,
              "p99": 0.00014254357665777206,
              "maximum": 0.0021213404834270477
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.047887131571769714,
              "candidate": 0.04576579108834267,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.6047127921237103,
            "cvrmse_percent": 11.283901042695474,
            "rms_normalized_rmse_percent": 2.502280152534667,
            "reference_energy": 15.155894616966995,
            "candidate_energy": 15.064244983457407,
            "relative_energy_error_percent": 0.6047127921237102,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.622772221158812e-07,
              "p90": 3.760669933399186e-05,
              "p95": 5.959550617262721e-05,
              "p99": 0.00013436668086797,
              "maximum": 0.0021213404834270477
            },
            "worst": {
              "global_sensor_index": 22,
              "local_sensor_index": 22,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.047887131571769714,
              "candidate": 0.04576579108834267,
              "position": [
                2.5,
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
      48,
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
        "identifier": "teaching_depth8_grid",
        "full_identifier": "teaching_depth8_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04684107795519001,
            "cvrmse_percent": 2.821610071633558,
            "rms_normalized_rmse_percent": 0.6149477330048871,
            "reference_energy": 9.146421276938781,
            "candidate_energy": 9.14213699461834,
            "relative_energy_error_percent": 0.046841077955190005,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.8442591428756714e-06,
              "p99": 5.678832530975342e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 23,
              "local_sensor_index": 23,
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
            "nmbe_percent": 80.71650064307919,
            "cvrmse_percent": 419.859684322724,
            "rms_normalized_rmse_percent": 24.0019658679525,
            "reference_energy": 3.2770156392832206,
            "candidate_energy": 5.922107988839066,
            "relative_energy_error_percent": 80.71650064307917,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002725674901739695,
              "p95": 0.00036337735582492314,
              "p99": 0.0006236592307686806,
              "maximum": 0.010827163234353065
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018228456377983093,
              "candidate": 0.02905561961233616,
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
            "nmbe_percent": 21.25666258897446,
            "cvrmse_percent": 110.73121326876819,
            "rms_normalized_rmse_percent": 23.998049367964608,
            "reference_energy": 12.423436916222002,
            "candidate_energy": 15.064244983457407,
            "relative_energy_error_percent": 21.25666258897446,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0002706727769691499,
              "p95": 0.00036313998862169683,
              "p99": 0.0006222955416887999,
              "maximum": 0.010827163234353065
            },
            "worst": {
              "global_sensor_index": 47,
              "local_sensor_index": 47,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.018228456377983093,
              "candidate": 0.02905561961233616,
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
      "bias_percent": 0.09158102334051017,
      "rms_normalized_error_percent": 0.21161093680764154,
      "absolute_error": {
        "p95": 0.10699094580812316,
        "p99": 0.1290813314403816,
        "maximum": 0.13273686702264342
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 13.78337538737606,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.21161093680764154
    },
    "overcast": {
      "bias_percent": 0.0564722092440864,
      "rms_normalized_error_percent": 0.193630465264064,
      "absolute_error": {
        "p95": 0.06821286678314208,
        "p99": 0.09889923095703125,
        "maximum": 0.10128021240234375
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.751224517822266,
      "reference_fraction_of_uniform": 0.6349115371704102,
      "rms_normalized_to_uniform_percent": 0.13523086398667916
    },
    "horizon": {
      "bias_percent": 1.0632315415434412,
      "rms_normalized_error_percent": 1.93358311974627,
      "absolute_error": {
        "p95": 0.042830451553009685,
        "p99": 0.09167569523978845,
        "maximum": 0.10779482674562746
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.3775766729211434,
      "reference_fraction_of_uniform": 0.09994479829540452,
      "rms_normalized_to_uniform_percent": 0.11786245343137594
    },
    "north": {
      "bias_percent": -68.61475816965428,
      "rms_normalized_error_percent": 103.09840563458836,
      "absolute_error": {
        "p95": 6.665041255473624e-05,
        "p99": 0.00011571368333534344,
        "maximum": 0.0001430556148989126
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.9918630641768686e-05,
      "reference_fraction_of_uniform": 1.4451198921960895e-06,
      "rms_normalized_to_uniform_percent": 0.00013623219726450984
    },
    "east": {
      "bias_percent": -0.03249771860748314,
      "rms_normalized_error_percent": 0.2728113814891013,
      "absolute_error": {
        "p95": 0.026857948303222655,
        "p99": 0.03724655628204346,
        "maximum": 0.03793525695800781
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.7839739322662354,
      "reference_fraction_of_uniform": 0.2019805610179901,
      "rms_normalized_to_uniform_percent": 0.06213791659285677
    },
    "south": {
      "bias_percent": 0.1274234736321722,
      "rms_normalized_error_percent": 0.23476258558991905,
      "absolute_error": {
        "p95": 0.068843674659729,
        "p99": 0.08922104358673098,
        "maximum": 0.09860086441040039
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.5862455368042,
      "reference_fraction_of_uniform": 0.6954932808876038,
      "rms_normalized_to_uniform_percent": 0.1503031897220477
    },
    "west": {
      "bias_percent": 0.05958915261382244,
      "rms_normalized_error_percent": 0.33005063436454757,
      "absolute_error": {
        "p95": 0.039032316207885734,
        "p99": 0.04754137039184571,
        "maximum": 0.048732757568359375
      },
      "worst_index": [
        31
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.686394691467285,
      "reference_fraction_of_uniform": 0.19490106403827667,
      "rms_normalized_to_uniform_percent": 0.07204078937273933
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
        "identifier": "teaching_depth8_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": -0.07049430534345205,
          "cvrmse_percent": 1.5042364414513638,
          "absolute_error_percentiles_lux": {
            "p50": 2.1340103149414062,
            "p90": 22.605651855468743,
            "p95": 36.126953125,
            "p99": 75.16133789062474
          },
          "maximum_absolute_error_lux": 334.0419921875,
          "worst": {
            "sensor_index": 15,
            "position": [
              1.5,
              0.5,
              0.75
            ],
            "hour_of_year": 1020.5,
            "foton_lux": 13908.7666015625,
            "radiance_lux": 13574.724609375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.45547659817351577,
            "maximum_error_percentage_points": 1.9486301369863028,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1836773842622946,
            "maximum_error_percentage_points": 0.7407548776392261,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1408761415525115,
            "maximum_error_percentage_points": 0.6538356164383572,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.15590753424657522,
            "maximum_error_percentage_points": 0.6542465753424693,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.021675228310502618,
            "maximum_error_percentage_points": 0.27698630136986324,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 58.333333333333336,
          "radiance_percent": 58.333333333333336,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.0833333333333335,
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
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004896725171235516,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth8_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
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
      "study_preparation_seconds": 0.006903833011165261,
      "weather_seconds": 0.09802845795638859,
      "metric_reduction_seconds": 0.054202625062316656,
      "write_seconds": 0.03023170807864517,
      "total_seconds": 0.18262362491805106,
      "cold_end_to_end_seconds": 0.18952745792921633,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.012908709002658725,
      "engine_upload_seconds": 0.000296333,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.03592741664033383,
      "engine_annual_reduction_seconds": 0.00042699999175965786,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.03592741664033383
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006903833011165261,
      "weather_seconds": 0.09207033296115696,
      "metric_reduction_seconds": 0.012058708001859486,
      "write_seconds": 0.030207165982574224,
      "total_seconds": 0.13450579205527902,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.13450579205527902,
      "raw_export_seconds": 0.012520916061475873,
      "engine_upload_seconds": 6.1834e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0004470832645893097,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.007209417060948908,
      "full": 0.024769208044745028
    }
  },
  "elapsed_seconds": 57.74191316694487,
  "result_class": "passed"
}
```
