# Foton report

Status: **failed**

```json
{
  "scene": "three_room_chain",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "three_room_chain",
    "category": "connections",
    "question": "Can daylight cross two successive internal glass partitions?",
    "interactions": [
      "borrowed_light",
      "serial_glazing",
      "paired_apertures"
    ],
    "room_count": 3,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 3,
    "apertures": 5,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 14.999999999999996
  },
  "sky_density": 2,
  "status": "failed",
  "passed": false,
  "model_sha256": "848fdc8e1fab3da490d9d4ccb829ec9a7c2bae463834873c24156dc39a42518b",
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
      "scene_fingerprint": 1666965602579954223,
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
      "solver_version": "0.2.0",
      "scene_fingerprint": 1666965602579954223,
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
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "bias_percent": -0.04451733069609173,
        "rms_normalized_error_percent": 0.7459934571017073,
        "absolute_error": {
          "p95": 1.210719347000122e-07,
          "p99": 9.124496136790706e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          11,
          543,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.49018890421638783,
        "rms_normalized_error_percent": 1.4186671733406047,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.0166406880784712e-07,
          "maximum": 2.361941005801782e-05
        },
        "worst_index": [
          17,
          153,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.3926457621321051,
        "rms_normalized_error_percent": 2.743125635136356,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 9.880026482278481e-06
        },
        "worst_index": [
          11,
          89,
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
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.05492606537042269,
        "rms_normalized_error_percent": 1.5781987499167114,
        "absolute_error": {
          "p95": 3.292615292593837e-05,
          "p99": 0.0001139128929935392,
          "maximum": 0.000369340181350708
        },
        "worst_index": [
          17,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": 0.6577586394448383,
        "rms_normalized_error_percent": 5.035752368729556,
        "absolute_error": {
          "p95": 3.1390309231937863e-06,
          "p99": 1.1549945338628867e-05,
          "maximum": 0.00023472867906093597
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.6508784670590287,
        "rms_normalized_error_percent": 8.590306285256622,
        "absolute_error": {
          "p95": 4.373693158754577e-07,
          "p99": 1.6729808749005203e-06,
          "maximum": 3.623376687755808e-05
        },
        "worst_index": [
          15,
          31,
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
        "identifier": "three_room_chain_0_grid",
        "bias_percent": 0.0019088792739185264,
        "rms_normalized_error_percent": 1.3010731422075315,
        "absolute_error": {
          "p95": 2.7350150048732758e-05,
          "p99": 9.134705178439565e-05,
          "maximum": 0.00032670795917510986
        },
        "worst_index": [
          18,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_1_grid",
        "bias_percent": -0.22345164829702077,
        "rms_normalized_error_percent": 3.988680434690062,
        "absolute_error": {
          "p95": 2.6687025638238993e-06,
          "p99": 9.367582879349203e-06,
          "maximum": 0.00022061215713620186
        },
        "worst_index": [
          10,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "three_room_chain_2_grid",
        "bias_percent": 0.741803258704794,
        "rms_normalized_error_percent": 8.625663719807573,
        "absolute_error": {
          "p95": 4.175081897983546e-07,
          "p99": 1.5926338363669587e-06,
          "maximum": 3.604181983973831e-05
        },
        "worst_index": [
          13,
          31,
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
        "run_count": 12,
        "half_run_count": 6,
        "oracle_stable": false,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.06592401356697045,
                "cvrmse_percent": 21.980769209703258,
                "rms_normalized_rmse_percent": 4.9699482549010865,
                "reference_energy": 5.711190753955179,
                "candidate_energy": 5.714955800122652,
                "relative_energy_error_percent": 0.06592401356697045,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.6737802525361524e-05,
                  "p99": 0.00016376271135716975,
                  "maximum": 0.00038392756444712494
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 363,
                  "rgb_channel": 0,
                  "reference": 0.004146445232133071,
                  "candidate": 0.003762517667685946
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.15829780896716106,
                "cvrmse_percent": 116.53525641984368,
                "rms_normalized_rmse_percent": 4.484233253614029,
                "reference_energy": 1.6987858887057392,
                "candidate_energy": 1.6960967478648747,
                "relative_energy_error_percent": 0.15829780896715914,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 6.827043762314132e-06,
                  "p95": 7.451296551153064e-05,
                  "p99": 0.00026109927275683696,
                  "maximum": 0.0006308900192379951
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02799278497695923,
                  "candidate": 0.028623674996197224
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.8479860143742134,
                "cvrmse_percent": 169.59515131701122,
                "rms_normalized_rmse_percent": 12.703479673926546,
                "reference_energy": 0.12286132953761353,
                "candidate_energy": 0.1239031764291667,
                "relative_energy_error_percent": 0.8479860143742137,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 3.004014312559398e-07,
                  "maximum": 0.00014058080463049316
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 89,
                  "rgb_channel": 0,
                  "reference": 0.0005795773176942021,
                  "candidate": 0.0007201581223246952
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -2.8472578764865086,
                "cvrmse_percent": 357.0548942858248,
                "rms_normalized_rmse_percent": 10.730128870125451,
                "reference_energy": 0.08760589175757616,
                "candidate_energy": 0.08511152610424233,
                "relative_energy_error_percent": 2.847257876486506,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.2678272078876018e-05,
                  "maximum": 0.0002519683912396431
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 150,
                  "rgb_channel": 0,
                  "reference": 6.55382367161413e-05,
                  "candidate": -0.00018643015452350178
                },
                "passed": false,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 2.0092156546187154,
                "cvrmse_percent": 538.6315559145042,
                "rms_normalized_rmse_percent": 25.106145651938508,
                "reference_energy": 0.011863940480907331,
                "candidate_energy": 0.012102312630304368,
                "relative_energy_error_percent": 2.0092156546187154,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 6.222556354866054e-05
                },
                "worst": {
                  "global_sensor_index": 63,
                  "local_sensor_index": 15,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00015830318686009073,
                  "candidate": 0.00022052875040875128
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -3.657882977304569,
                "cvrmse_percent": 580.4847308593127,
                "rms_normalized_rmse_percent": 18.873133783562825,
                "reference_energy": 0.012737058035099835,
                "candidate_energy": 0.012271151357424515,
                "relative_energy_error_percent": 3.657882977304569,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 7.018948129674143e-07,
                  "maximum": 8.61260626455381e-05
                },
                "worst": {
                  "global_sensor_index": 60,
                  "local_sensor_index": 12,
                  "sky_patch_index": 32,
                  "rgb_channel": 0,
                  "reference": 0.00017102410796117815,
                  "candidate": 8.489804531564005e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 157.27462503127754,
            "full": 417.4878749763593
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 150.35387501120567,
            "full": 405.09966702666134
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 146.5522910002619,
            "full": 398.7423749640584
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.83262500632554,
            "full": 412.9024170106277
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.7241670731455,
            "full": 428.8781250361353
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.92612493410707,
            "full": 412.4012499814853
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 144.63237498421222,
            "full": 408.7523340713233
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 142.52333308104426,
            "full": 418.94633299671113
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.0522091044113,
            "full": 427.6079999981448
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 156.75204095896333,
            "full": 408.53762498591095
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.38733400776982,
            "full": 413.00091694574803
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 145.14150004833937,
            "full": 407.8255830099806
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.10066144105240074,
                "cvrmse_percent": 19.77089775262236,
                "rms_normalized_rmse_percent": 4.471730097630549,
                "reference_energy": 5.715458408229779,
                "candidate_energy": 5.709705145433304,
                "relative_energy_error_percent": 0.10066144105240074,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.430348053574562e-05,
                  "p99": 0.00015133347478695072,
                  "maximum": 0.00037280446849763393
                },
                "worst": {
                  "global_sensor_index": 12,
                  "local_sensor_index": 12,
                  "sky_patch_index": 153,
                  "rgb_channel": 0,
                  "reference": 0.0016378645086660981,
                  "candidate": 0.002010668977163732
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.15894906408264495,
                "cvrmse_percent": 56.57199467406918,
                "rms_normalized_rmse_percent": 3.0056682897229625,
                "reference_energy": 3.0291520905130724,
                "candidate_energy": 3.033966899410583,
                "relative_energy_error_percent": 0.15894906408264498,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.919974922439451e-08,
                  "p90": 1.6422633052570745e-05,
                  "p95": 6.357021629810333e-05,
                  "p99": 0.00021549108751059933,
                  "maximum": 0.0006921738386154175
                },
                "worst": {
                  "global_sensor_index": 6,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03266710415482521,
                  "candidate": 0.03197493031620979
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.37355161586973284,
                "cvrmse_percent": 150.90512491934874,
                "rms_normalized_rmse_percent": 11.280657511297711,
                "reference_energy": 0.12410464906162133,
                "candidate_energy": 0.12364105413968218,
                "relative_energy_error_percent": 0.37355161586973284,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 1.4754277799510002e-07,
                  "maximum": 0.00012695847181021236
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 14,
                  "sky_patch_index": 32,
                  "rgb_channel": 0,
                  "reference": 0.0001374727908114437,
                  "candidate": 0.00026443126262165606
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.673906630008699,
                "cvrmse_percent": 166.6180097247037,
                "rms_normalized_rmse_percent": 8.287946378965902,
                "reference_energy": 0.19935814251385153,
                "candidate_energy": 0.20070163025371457,
                "relative_energy_error_percent": 0.673906630008699,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.4535552256566007e-06,
                  "p95": 4.3249763450603496e-06,
                  "p99": 1.4035519370736312e-05,
                  "maximum": 0.00023687700740993023
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 15,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.005194036988541484,
                  "candidate": 0.005430913995951414
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 3.4245524111493206,
                "cvrmse_percent": 577.0261829082802,
                "rms_normalized_rmse_percent": 27.479391771525847,
                "reference_energy": 0.01181815484778781,
                "candidate_energy": 0.012222873754581087,
                "relative_energy_error_percent": 3.42455241114932,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 8.431214519077912e-05
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.00011813150194939226,
                  "candidate": 0.00020244364714017138
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -3.4086153208721885,
                "cvrmse_percent": 474.9919400614552,
                "rms_normalized_rmse_percent": 24.39801811716867,
                "reference_energy": 0.02733846294147213,
                "candidate_energy": 0.026406599905158146,
                "relative_energy_error_percent": 3.4086153208721885,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7496775228664774e-07,
                  "p95": 4.661357486668294e-07,
                  "p99": 2.633415168418189e-06,
                  "maximum": 0.0001682484471530188
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 8.103829895844683e-05,
                  "candidate": -8.721014819457196e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 217.0602090191096,
            "full": 5198.985041002743
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 210.84049995988607,
            "full": 5200.3611670807
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 216.6256250347942,
            "full": 5152.939624967985
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.27749998494983,
            "full": 5283.781290985644
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.11860407439450517,
                "cvrmse_percent": 20.22453098538562,
                "rms_normalized_rmse_percent": 4.576842673130118,
                "reference_energy": 5.715101975858715,
                "candidate_energy": 5.708323632059546,
                "relative_energy_error_percent": 0.11860407439450518,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.435455775819719e-05,
                  "p99": 0.00015241914370562844,
                  "maximum": 0.00034923976636491716
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 88,
                  "rgb_channel": 0,
                  "reference": 0.001329551450908184,
                  "candidate": 0.000980311684543267
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.2597928085055097,
                "cvrmse_percent": 58.66937067508736,
                "rms_normalized_rmse_percent": 3.124100781056452,
                "reference_energy": 3.0332911756511507,
                "candidate_energy": 3.0411714479865246,
                "relative_energy_error_percent": 0.2597928085055097,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.26354489491132e-08,
                  "p90": 1.6567297279834747e-05,
                  "p95": 6.528061931021512e-05,
                  "p99": 0.00022635175118921282,
                  "maximum": 0.0008666012436151505
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03439590334892273,
                  "candidate": 0.03526250459253788
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.5560982128931347,
                "cvrmse_percent": 146.29255944672838,
                "rms_normalized_rmse_percent": 10.91258552657921,
                "reference_energy": 0.12442255729200724,
                "candidate_energy": 0.12511446890954403,
                "relative_energy_error_percent": 0.5560982128931348,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.263766090976771e-07,
                  "maximum": 0.00014410314906854182
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 0.0006822057475801557,
                  "candidate": 0.0005381025985116139
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -1.108628381881218,
                "cvrmse_percent": 173.4220128413984,
                "rms_normalized_rmse_percent": 8.497016995004575,
                "reference_energy": 0.20238658182091385,
                "candidate_energy": 0.20014286673372794,
                "relative_energy_error_percent": 1.1086283818812182,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.517100938348449e-06,
                  "p95": 4.383407542718487e-06,
                  "p99": 1.669991141284278e-05,
                  "maximum": 0.00026779784820973873
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0055034044198691845,
                  "candidate": 0.005235606571659446
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 1.1987254761627177,
                "cvrmse_percent": 638.5317800993932,
                "rms_normalized_rmse_percent": 29.535354884643482,
                "reference_energy": 0.012151185129368969,
                "candidate_energy": 0.01229684448117041,
                "relative_energy_error_percent": 1.1987254761627177,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00010974327324220212
                },
                "worst": {
                  "global_sensor_index": 61,
                  "local_sensor_index": 13,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 3.374527568666963e-05,
                  "candidate": 0.00014348854892887175
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.8763368517074192,
                "cvrmse_percent": 393.3700630862607,
                "rms_normalized_rmse_percent": 20.211431323935223,
                "reference_energy": 0.027040661132605948,
                "candidate_energy": 0.026803693854155597,
                "relative_energy_error_percent": 0.8763368517074192,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7736644508659083e-07,
                  "p95": 4.6424459299032605e-07,
                  "p99": 2.7086871057235573e-06,
                  "maximum": 0.00012988851904083276
                },
                "worst": {
                  "global_sensor_index": 61,
                  "local_sensor_index": 13,
                  "sky_patch_index": 91,
                  "rgb_channel": 0,
                  "reference": 7.157110758271301e-05,
                  "candidate": -5.831741145811975e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 215.76958301011473,
            "full": 5484.703082940541
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.01545905973762,
            "full": 5518.353834049776
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 212.15995901729912,
            "full": 5451.335082994774
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 208.2448749570176,
            "full": 5490.165667026304
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "three_room_chain_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.053462178643755534,
                "cvrmse_percent": 11.617282705563388,
                "rms_normalized_rmse_percent": 2.6289537321258996,
                "reference_energy": 5.712267843920131,
                "candidate_energy": 5.7092139410808045,
                "relative_energy_error_percent": 0.05346217864375554,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3147847969084978e-05,
                  "p99": 8.748937980271836e-05,
                  "maximum": 0.00019897462334483862
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 362,
                  "rgb_channel": 0,
                  "reference": 0.004017867613583803,
                  "candidate": 0.0038188929902389646
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.11341908567724228,
                "cvrmse_percent": 32.22569223613774,
                "rms_normalized_rmse_percent": 1.7179246711723526,
                "reference_energy": 3.036648112070935,
                "candidate_energy": 3.0400922505948813,
                "relative_energy_error_percent": 0.11341908567724228,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.1830602154059306e-08,
                  "p90": 1.1338195690768771e-05,
                  "p95": 3.882101736962795e-05,
                  "p99": 0.00012438851481419907,
                  "maximum": 0.0003881901502609253
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.036514004692435265,
                  "candidate": 0.03690219484269619
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "three_room_chain_1_grid",
            "start_sensor_index": 24,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.4987283015055137,
                "cvrmse_percent": 91.80552446546618,
                "rms_normalized_rmse_percent": 6.923519163749283,
                "reference_energy": 0.1242640293252748,
                "candidate_energy": 0.12364428944243855,
                "relative_energy_error_percent": 0.4987283015055138,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 8.31498942943647e-07,
                  "maximum": 8.289534889627248e-05
                },
                "worst": {
                  "global_sensor_index": 40,
                  "local_sensor_index": 16,
                  "sky_patch_index": 94,
                  "rgb_channel": 0,
                  "reference": 0.00022830499801784754,
                  "candidate": 0.00031120034691412
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.18567379563951208,
                "cvrmse_percent": 105.35637742752697,
                "rms_normalized_rmse_percent": 5.208103406879965,
                "reference_energy": 0.20116379963725706,
                "candidate_energy": 0.20153730809949622,
                "relative_energy_error_percent": 0.18567379563951208,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8403550825496495e-06,
                  "p95": 3.1719006301500485e-06,
                  "p99": 1.2271109881112286e-05,
                  "maximum": 0.00016502552898600698
                },
                "worst": {
                  "global_sensor_index": 37,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0019313785596750677,
                  "candidate": 0.0017663530306890607
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "three_room_chain_2_grid",
            "start_sensor_index": 48,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.9184078617519351,
                "cvrmse_percent": 256.33010253603305,
                "rms_normalized_rmse_percent": 12.092496074595575,
                "reference_energy": 0.01219605659480294,
                "candidate_energy": 0.012308066137393325,
                "relative_energy_error_percent": 0.918407861751935,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 3.359789843671024e-05
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 10,
                  "sky_patch_index": 90,
                  "rgb_channel": 0,
                  "reference": 0.00013440815382637084,
                  "candidate": 0.00016800605226308107
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -2.091090240934027,
                "cvrmse_percent": 210.7369838008535,
                "rms_normalized_rmse_percent": 10.92556951487464,
                "reference_energy": 0.027471748240216698,
                "candidate_energy": 0.02689728919375156,
                "relative_energy_error_percent": 2.091090240934027,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7427695198080073e-07,
                  "p95": 4.806819902114512e-07,
                  "p99": 1.8853184023725793e-06,
                  "maximum": 5.246857472229749e-05
                },
                "worst": {
                  "global_sensor_index": 61,
                  "local_sensor_index": 13,
                  "sky_patch_index": 32,
                  "rgb_channel": 0,
                  "reference": 7.99737754277885e-05,
                  "candidate": 2.7505200705491006e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 345.1427499530837,
            "full": 9602.385624893941
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 327.59916700888425,
            "full": 9549.09458302427
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 347.1326660364866,
            "full": 9523.5202080803
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 343.3344590011984,
            "full": 9588.830832974054
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 10858.259915956296,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/three_room_chain/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 43599.562625051476,
      "worker_pool_size": 12,
      "invocation_count": 5
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2448781164189055,
            "cvrmse_percent": 3.413904707325956,
            "rms_normalized_rmse_percent": 0.7731968023365993,
            "reference_energy": 5.711498051196358,
            "candidate_energy": 5.697511842349286,
            "relative_energy_error_percent": 0.24487811641890547,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2654421627521515e-07,
              "p99": 1.9674193936225476e-05,
              "maximum": 0.0001028992046485655
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.0001028992046485655,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.6539945869668317,
            "cvrmse_percent": 32.99002157726627,
            "rms_normalized_rmse_percent": 1.7582811379185816,
            "reference_energy": 3.0376130464315416,
            "candidate_energy": 3.017747221534881,
            "relative_energy_error_percent": 0.6539945869668318,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.000000058430487e-08,
              "p90": 1.2124241038691252e-05,
              "p95": 2.175286499550566e-05,
              "p99": 5.740866454289042e-05,
              "maximum": 0.0010394714772701263
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036708101630210876,
              "candidate": 0.03566863015294075,
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
            "nmbe_percent": -0.3869196923663572,
            "cvrmse_percent": 11.272425352717827,
            "rms_normalized_rmse_percent": 1.730432118922382,
            "reference_energy": 8.7491110976279,
            "candidate_energy": 8.715259063884167,
            "relative_energy_error_percent": 0.38691969236635726,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.1255313438596204e-05,
              "p95": 1.9606814021244645e-05,
              "p99": 5.344562523532637e-05,
              "maximum": 0.0010394714772701263
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.036708101630210876,
              "candidate": 0.03566863015294075,
              "position": [
                2.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -1.0916299628620405,
            "cvrmse_percent": 22.678819353068285,
            "rms_normalized_rmse_percent": 1.7142543404371473,
            "reference_energy": 0.12371627908974858,
            "candidate_energy": 0.12236575511826686,
            "relative_energy_error_percent": 1.0916299628620405,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0021918569690686e-06,
              "maximum": 2.273775498906616e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 8,
              "sky_patch_index": 61,
              "rgb_channel": 0,
              "reference": 2.273775498906616e-05,
              "candidate": 0.0,
              "position": [
                2.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 1.165417272832167,
            "cvrmse_percent": 69.26788884136599,
            "rms_normalized_rmse_percent": 3.4396534329359656,
            "reference_energy": 0.2015884312309204,
            "candidate_energy": 0.20393777762851695,
            "relative_energy_error_percent": 1.165417272832167,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.962955820999923e-06,
              "p95": 3.199132152076345e-06,
              "p99": 9.13847688934763e-06,
              "maximum": 0.0001350073143839836
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0025138126220554113,
              "candidate": 0.002648819936439395,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.3070421037341364,
            "cvrmse_percent": 42.33950531711527,
            "rms_normalized_rmse_percent": 3.3927609563594805,
            "reference_energy": 0.325304710320669,
            "candidate_energy": 0.3263035327467838,
            "relative_energy_error_percent": 0.30704210373413643,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.9030987914447905e-06,
              "p95": 3.0867151963320794e-06,
              "p99": 8.34532879707687e-06,
              "maximum": 0.0001350073143839836
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0025138126220554113,
              "candidate": 0.002648819936439395,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.20226535278867852,
            "cvrmse_percent": 32.433418705225215,
            "rms_normalized_rmse_percent": 1.5363714302206832,
            "reference_energy": 0.01226061213382934,
            "candidate_energy": 0.012235813163442799,
            "relative_energy_error_percent": 0.20226535278867852,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955624485271983e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627300581429154e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 5.374241478061532,
            "cvrmse_percent": 181.44768364284346,
            "rms_normalized_rmse_percent": 9.345490908947227,
            "reference_energy": 0.027175967857091976,
            "candidate_energy": 0.028636469993732483,
            "relative_energy_error_percent": 5.374241478061533,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8999999440438842e-07,
              "p95": 4.5435248452463384e-07,
              "p99": 1.9528475434071873e-06,
              "maximum": 6.433259113691747e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00036677741445600986,
              "candidate": 0.00043111000559292734,
              "position": [
                2.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 3.640536696094028,
            "cvrmse_percent": 125.12736886311464,
            "rms_normalized_rmse_percent": 9.352274133640794,
            "reference_energy": 0.03943657999092132,
            "candidate_energy": 0.04087228315717528,
            "relative_energy_error_percent": 3.640536696094028,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.8999999440438842e-07,
              "p95": 4.539655060753489e-07,
              "p99": 1.9689458383709004e-06,
              "maximum": 6.433259113691747e-05
            },
            "worst": {
              "global_sensor_index": 56,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00036677741445600986,
              "candidate": 0.00043111000559292734,
              "position": [
                2.5,
                11.5,
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
        "identifier": "three_room_chain_0_grid",
        "full_identifier": "three_room_chain_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2448781164189055,
            "cvrmse_percent": 3.413904707325956,
            "rms_normalized_rmse_percent": 0.7731968023365993,
            "reference_energy": 5.711498051196358,
            "candidate_energy": 5.697511842349286,
            "relative_energy_error_percent": 0.24487811641890547,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2654421627521515e-07,
              "p99": 1.9674193936225476e-05,
              "maximum": 0.0001028992046485655
            },
            "worst": {
              "global_sensor_index": 8,
              "local_sensor_index": 8,
              "sky_patch_index": 121,
              "rgb_channel": 0,
              "reference": 0.0001028992046485655,
              "candidate": 0.0,
              "position": [
                2.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 77.61729583129551,
            "cvrmse_percent": 848.217844827884,
            "rms_normalized_rmse_percent": 32.6427083178592,
            "reference_energy": 1.6990165329401243,
            "candidate_energy": 3.017747221534881,
            "relative_energy_error_percent": 77.61729583129551,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.181999924592674e-05,
              "p95": 8.231494575738907e-05,
              "p99": 0.00014450729286181728,
              "maximum": 0.009630757384002209
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014586851932108402,
              "candidate": 0.02421760931611061,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 17.60666502891339,
            "cvrmse_percent": 194.45553143802928,
            "rms_normalized_rmse_percent": 32.63997686804472,
            "reference_energy": 7.410514584136482,
            "candidate_energy": 8.715259063884167,
            "relative_energy_error_percent": 17.60666502891339,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 6.125000072643161e-05,
              "p95": 8.218824950745329e-05,
              "p99": 0.0001452085802156932,
              "maximum": 0.009630757384002209
            },
            "worst": {
              "global_sensor_index": 20,
              "local_sensor_index": 20,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.014586851932108402,
              "candidate": 0.02421760931611061,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "full_identifier": "three_room_chain_1_grid",
        "start_sensor_index": 24,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -1.0916299628620405,
            "cvrmse_percent": 22.678819353068285,
            "rms_normalized_rmse_percent": 1.7142543404371473,
            "reference_energy": 0.12371627908974858,
            "candidate_energy": 0.12236575511826686,
            "relative_energy_error_percent": 1.0916299628620405,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 1.0021918569690686e-06,
              "maximum": 2.273775498906616e-05
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 8,
              "sky_patch_index": 61,
              "rgb_channel": 0,
              "reference": 2.273775498906616e-05,
              "candidate": 0.0,
              "position": [
                2.5,
                7.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 137.06890637591144,
            "cvrmse_percent": 1633.4721003630523,
            "rms_normalized_rmse_percent": 48.17325385723337,
            "reference_energy": 0.0860246840237835,
            "candidate_energy": 0.20393777762851695,
            "relative_energy_error_percent": 137.06890637591147,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.625918336387258e-06,
              "p95": 8.819999493425712e-06,
              "p99": 2.2265405641519406e-05,
              "maximum": 0.001588030019775033
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.003710729768499732,
              "candidate": 0.005298759788274765,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 55.57453723055368,
            "cvrmse_percent": 669.8036442877094,
            "rms_normalized_rmse_percent": 48.16171445549991,
            "reference_energy": 0.20974096311353208,
            "candidate_energy": 0.3263035327467838,
            "relative_energy_error_percent": 55.57453723055367,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.529999841906829e-06,
              "p95": 8.580000212532468e-06,
              "p99": 2.2046097546990452e-05,
              "maximum": 0.001588030019775033
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.003710729768499732,
              "candidate": 0.005298759788274765,
              "position": [
                2.5,
                4.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "full_identifier": "three_room_chain_2_grid",
        "start_sensor_index": 48,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.20226535278867852,
            "cvrmse_percent": 32.433418705225215,
            "rms_normalized_rmse_percent": 1.5363714302206832,
            "reference_energy": 0.01226061213382934,
            "candidate_energy": 0.012235813163442799,
            "relative_energy_error_percent": 0.20226535278867852,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 6.955624485271983e-06
            },
            "worst": {
              "global_sensor_index": 53,
              "local_sensor_index": 5,
              "sky_patch_index": 89,
              "rgb_channel": 0,
              "reference": 2.667167609615717e-05,
              "candidate": 3.3627300581429154e-05,
              "position": [
                1.5,
                10.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 134.2141336699632,
            "cvrmse_percent": 1828.2642782773194,
            "rms_normalized_rmse_percent": 57.71918211273275,
            "reference_energy": 0.012226619096388447,
            "candidate_energy": 0.028636469993732483,
            "relative_energy_error_percent": 134.2141336699632,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.500000053056283e-07,
              "p95": 4.599999954280065e-07,
              "p99": 4.72037731924486e-06,
              "maximum": 0.00020446321286726743
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00015896679542493075,
              "candidate": 0.0003634300082921982,
              "position": [
                2.5,
                8.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 66.91263611190953,
            "cvrmse_percent": 912.115518510965,
            "rms_normalized_rmse_percent": 57.67191057122494,
            "reference_energy": 0.024487231230217787,
            "candidate_energy": 0.04087228315717528,
            "relative_energy_error_percent": 66.91263611190952,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.500000053056283e-07,
              "p95": 4.599999954280065e-07,
              "p99": 4.5009374844083575e-06,
              "maximum": 0.00020446321286726743
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00015896679542493075,
              "candidate": 0.0003634300082921982,
              "position": [
                2.5,
                8.5,
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
      "bias_percent": -0.03692733325452082,
      "rms_normalized_error_percent": 0.1965514451244919,
      "absolute_error": {
        "p95": 0.06410534151885076,
        "p99": 0.12278492961662987,
        "maximum": 0.1272577544006186
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.708250876258004,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1965514451244919
    },
    "overcast": {
      "bias_percent": -0.03763669656590127,
      "rms_normalized_error_percent": 0.13419527310615612,
      "absolute_error": {
        "p95": 0.030254733562469487,
        "p99": 0.06641211509704592,
        "maximum": 0.06895804405212402
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6918046474456787,
      "reference_fraction_of_uniform": 0.6467488408088684,
      "rms_normalized_to_uniform_percent": 0.09541242117020839
    },
    "horizon": {
      "bias_percent": 0.4619932479403049,
      "rms_normalized_error_percent": 1.778047066077723,
      "absolute_error": {
        "p95": 0.041378477128055716,
        "p99": 0.07223358278441742,
        "maximum": 0.07383687567901243
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.6126500770341886,
      "reference_fraction_of_uniform": 0.10732711128418486,
      "rms_normalized_to_uniform_percent": 0.11719102209921131
    },
    "north": {
      "bias_percent": -96.605634125302,
      "rms_normalized_error_percent": 98.43943662066283,
      "absolute_error": {
        "p95": 9.827536196098674e-05,
        "p99": 0.00042772896546466676,
        "maximum": 0.0004518349692261836
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.1432169887702912e-05,
      "reference_fraction_of_uniform": 3.754594899874064e-06,
      "rms_normalized_to_uniform_percent": 0.0005244597669375879
    },
    "east": {
      "bias_percent": 0.13863617631861685,
      "rms_normalized_error_percent": 0.21556826170556861,
      "absolute_error": {
        "p95": 0.011557656526565553,
        "p99": 0.02503341913223274,
        "maximum": 0.033211708068847656
      },
      "worst_index": [
        2
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.0872241258621216,
      "reference_fraction_of_uniform": 0.19046536087989807,
      "rms_normalized_to_uniform_percent": 0.04352822502030727
    },
    "south": {
      "bias_percent": -0.06228324426850846,
      "rms_normalized_error_percent": 0.2805095435347426,
      "absolute_error": {
        "p95": 0.05809977054595948,
        "p99": 0.11017939090728775,
        "maximum": 0.12653732299804688
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.92702054977417,
      "reference_fraction_of_uniform": 0.6879551410675049,
      "rms_normalized_to_uniform_percent": 0.18306290424116148
    },
    "west": {
      "bias_percent": 0.005969122451318331,
      "rms_normalized_error_percent": 0.17483130140252182,
      "absolute_error": {
        "p95": 0.011830943822860722,
        "p99": 0.018297302722930953,
        "maximum": 0.023494958877563477
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.100180983543396,
      "reference_fraction_of_uniform": 0.1927352100610733,
      "rms_normalized_to_uniform_percent": 0.035575131344779964
    }
  },
  "annual": {
    "schema_version": 1,
    "oracle": "converged-coefficients",
    "passed": false,
    "occupied_hours": 3650,
    "structural": {
      "sun_up_hours_match": true,
      "grid_ids_match": true,
      "grid_counts_match": true
    },
    "grids": [
      {
        "identifier": "three_room_chain_0_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.04009984661297616,
          "cvrmse_percent": 1.5321149415554487,
          "absolute_error_percentiles_lux": {
            "p50": 2.41107177734375,
            "p90": 28.55940246582033,
            "p95": 44.823211669921825,
            "p99": 95.63808776855464
          },
          "maximum_absolute_error_lux": 462.6435546875,
          "worst": {
            "sensor_index": 12,
            "position": [
              3.5,
              3.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 10219.71875,
            "radiance_lux": 10682.3623046875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.20998858447488603,
            "maximum_error_percentage_points": 0.8179452054794538,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07695071188465914,
            "maximum_error_percentage_points": 0.30193500197096057,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.05776255707762538,
            "maximum_error_percentage_points": 0.3836986301369869,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.0626198630136982,
            "maximum_error_percentage_points": 0.30602739726026584,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03702054794520531,
            "maximum_error_percentage_points": 0.1116438356164382,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 91.66666666666667,
          "radiance_percent": 91.66666666666667,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_1_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.5842179514334008,
          "cvrmse_percent": 9.91294841774594,
          "absolute_error_percentiles_lux": {
            "p50": 0.3960580825805664,
            "p90": 4.788248062133792,
            "p95": 7.619352054595934,
            "p99": 15.776693325042716
          },
          "maximum_absolute_error_lux": 89.8798828125,
          "worst": {
            "sensor_index": 10,
            "position": [
              2.5,
              5.5,
              0.75
            ],
            "hour_of_year": 828.5,
            "foton_lux": 2304.154052734375,
            "radiance_lux": 2214.274169921875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.042562785388127806,
            "maximum_error_percentage_points": 0.520410958904109,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.16144860455548457,
            "maximum_error_percentage_points": 0.43702777838872464,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.2907191780821936,
            "maximum_error_percentage_points": 1.7513698630137071,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.29041666666666677,
            "maximum_error_percentage_points": 1.7513698630136965,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.00021689497716894981,
            "maximum_error_percentage_points": 0.003972602739725994,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "three_room_chain_2_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 1.6658351830435743,
          "cvrmse_percent": 16.973945323099247,
          "absolute_error_percentiles_lux": {
            "p50": 0.06311804056167603,
            "p90": 0.7536314010620119,
            "p95": 1.2626469135284413,
            "p99": 2.716699037551876
          },
          "maximum_absolute_error_lux": 23.05517578125,
          "worst": {
            "sensor_index": 15,
            "position": [
              3.5,
              8.5,
              0.75
            ],
            "hour_of_year": 348.5,
            "foton_lux": 558.4498901367188,
            "radiance_lux": 581.5050659179688
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.0014269406392694074,
            "maximum_error_percentage_points": 0.024794520547945204,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04974601341808536,
            "maximum_error_percentage_points": 0.2773921686892309,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.004029680365295718,
            "maximum_error_percentage_points": 0.02945205479451829,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.004029680365296807,
            "maximum_error_percentage_points": 0.02945205479452062,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      }
    ]
  },
  "outcomes": {
    "numerical_correctness": "failed",
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
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004717465753415695,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004729539008989647,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.00478594218214895,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.0045205479452054,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004383561643835632,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.004794520547942938,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.004520547945205067,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.004383561643834355,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "three_room_chain_0_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          },
          {
            "identifier": "three_room_chain_1_grid",
            "maximum_error_percentage_points": 0.003972602739725994,
            "passed": true
          },
          {
            "identifier": "three_room_chain_2_grid",
            "maximum_error_percentage_points": 0.0,
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
      "study_preparation_seconds": 0.01249241700861603,
      "weather_seconds": 0.12981941702309996,
      "metric_reduction_seconds": 0.2602753749815747,
      "write_seconds": 0.06169383297674358,
      "total_seconds": 0.4519963329657912,
      "cold_end_to_end_seconds": 0.46448874997440726,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.027891083038412035,
      "engine_upload_seconds": 0.0008625,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.2053845414193347,
      "engine_annual_reduction_seconds": 0.0029739999445155263,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.2053845414193347
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.01249241700861603,
      "weather_seconds": 0.11637220892589539,
      "metric_reduction_seconds": 0.04624691605567932,
      "write_seconds": 0.04720499995164573,
      "total_seconds": 0.21002183307427913,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.21002183307427913,
      "raw_export_seconds": 0.019007958006113768,
      "engine_upload_seconds": 8.3875e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0030898749828338623,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015016083023510873,
      "full": 0.199569332995452
    }
  },
  "elapsed_seconds": 149.56199345795903,
  "result_class": "accuracy_failure"
}
```
