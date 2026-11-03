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
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "5f00d8ac35058fd32921af39f4579b5f7680f386b71cf1598db44f3751ead4bf",
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
      "scene_fingerprint": 18345719022415901050,
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
      "scene_fingerprint": 18345719022415901050,
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
        "identifier": "teaching_reflectance70_grid",
        "bias_percent": -0.02181882161705929,
        "rms_normalized_error_percent": 0.7580187937848226,
        "absolute_error": {
          "p95": 1.1152587831020355e-07,
          "p99": 1.1820709914900362e-05,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          17,
          543,
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
        "identifier": "teaching_reflectance70_grid",
        "bias_percent": 0.850470259640372,
        "rms_normalized_error_percent": 1.505143137576275,
        "absolute_error": {
          "p95": 4.734564572572708e-05,
          "p99": 0.00012572947889566422,
          "maximum": 0.0016387440264225006
        },
        "worst_index": [
          25,
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
        "identifier": "teaching_reflectance70_grid",
        "bias_percent": -0.00842499358270035,
        "rms_normalized_error_percent": 0.8295149582016158,
        "absolute_error": {
          "p95": 3.9383769035339355e-05,
          "p99": 0.00010343664325773716,
          "maximum": 0.0006052851676940918
        },
        "worst_index": [
          15,
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_reflectance70_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.15770534755199203,
                "cvrmse_percent": 27.981645321177496,
                "rms_normalized_rmse_percent": 6.545951011603341,
                "reference_energy": 8.945951632096694,
                "candidate_energy": 8.960059876209925,
                "relative_energy_error_percent": 0.15770534755199203,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.466890383511782e-05,
                  "p99": 0.00021006399765610695,
                  "maximum": 0.0006383184809237719
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 268,
                  "rgb_channel": 0,
                  "reference": 0.0030488419579342008,
                  "candidate": 0.0036871604388579726
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.26072592752726603,
                "cvrmse_percent": 100.12603065301626,
                "rms_normalized_rmse_percent": 4.261198592122959,
                "reference_energy": 4.337786992276918,
                "candidate_energy": 4.326477256907147,
                "relative_energy_error_percent": 0.26072592752726603,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.556846309540575e-05,
                  "p95": 0.00011288887981208973,
                  "p99": 0.00035287460195831954,
                  "maximum": 0.0015158988535404205
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03771944157779217,
                  "candidate": 0.03923534043133259
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 111.12479097209871,
            "full": 241.1116249859333
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 119.67433395329863,
            "full": 217.72816695738584
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 106.22366704046726,
            "full": 235.66250002477318
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 112.74125007912517,
            "full": 219.4613330066204
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
            "identifier": "teaching_reflectance70_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04835496629842243,
                "cvrmse_percent": 21.19970502985839,
                "rms_normalized_rmse_percent": 4.965439035170404,
                "reference_energy": 8.952611083575448,
                "candidate_energy": 8.948282051503156,
                "relative_energy_error_percent": 0.048354966298422425,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.709605127573013e-05,
                  "p99": 0.00016344955656677485,
                  "maximum": 0.0003449369687587023
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 308,
                  "rgb_channel": 0,
                  "reference": 0.0033423469867557287,
                  "candidate": 0.003687283955514431
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.008086810421498655,
                "cvrmse_percent": 26.509719182969928,
                "rms_normalized_rmse_percent": 1.726133496828666,
                "reference_energy": 11.767015631748656,
                "candidate_energy": 11.767967207995063,
                "relative_energy_error_percent": 0.008086810421498655,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.439864629394833e-08,
                  "p90": 3.7244775376166245e-05,
                  "p95": 8.165068720700219e-05,
                  "p99": 0.00024089645012281835,
                  "maximum": 0.001295473426580429
                },
                "worst": {
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07089891284704208,
                  "candidate": 0.06960343942046165
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 152.03266602475196,
            "full": 2402.497500064783
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 155.2865409757942,
            "full": 2463.463042047806
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.2161669516936,
            "full": 2401.2140420963988
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 151.41137491445988,
            "full": 2461.2052079755813
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
            "identifier": "teaching_reflectance70_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.036865285083779654,
                "cvrmse_percent": 20.388326605870002,
                "rms_normalized_rmse_percent": 4.772590157289783,
                "reference_energy": 8.949710934708492,
                "candidate_energy": 8.946411598258237,
                "relative_energy_error_percent": 0.036865285083779654,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 5.606585182249546e-05,
                  "p99": 0.0001611184561625123,
                  "maximum": 0.0003489660448394716
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 94,
                  "rgb_channel": 0,
                  "reference": 0.0008845244301483035,
                  "candidate": 0.001233490474987775
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.047380093508392666,
                "cvrmse_percent": 27.260549792260058,
                "rms_normalized_rmse_percent": 1.7851825629368254,
                "reference_energy": 11.948907287986117,
                "candidate_energy": 11.943245884539838,
                "relative_energy_error_percent": 0.04738009350839266,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 8.40582359273867e-08,
                  "p90": 3.750854521058509e-05,
                  "p95": 8.449768938589841e-05,
                  "p99": 0.00025198201183229685,
                  "maximum": 0.001164119690656662
                },
                "worst": {
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.06432368978857994,
                  "candidate": 0.06315957009792328
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 147.4240419920534,
            "full": 2709.2177500016987
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.32262496929616,
            "full": 2671.017957967706
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 162.68462501466274,
            "full": 2756.697625038214
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 139.38837498426437,
            "full": 2697.2969999769703
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
            "identifier": "teaching_reflectance70_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04737822372792456,
                "cvrmse_percent": 10.038711647998952,
                "rms_normalized_rmse_percent": 2.3524475902871944,
                "reference_energy": 8.952390620328515,
                "candidate_energy": 8.948149136671418,
                "relative_energy_error_percent": 0.04737822372792457,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.378749195486307e-05,
                  "p99": 7.638955139555037e-05,
                  "maximum": 0.00020691039389930665
                },
                "worst": {
                  "global_sensor_index": 30,
                  "local_sensor_index": 30,
                  "sky_patch_index": 155,
                  "rgb_channel": 0,
                  "reference": 0.0005521991988644004,
                  "candidate": 0.00034528880496509373
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.08404469916053853,
                "cvrmse_percent": 14.217076572228738,
                "rms_normalized_rmse_percent": 0.9301606320018369,
                "reference_energy": 11.9471281474925,
                "candidate_energy": 11.937087219582615,
                "relative_energy_error_percent": 0.08404469916053851,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.44109476866106e-08,
                  "p90": 2.537964537623339e-05,
                  "p95": 4.932243609800935e-05,
                  "p99": 0.00012565907672978938,
                  "maximum": 0.0006698369979858398
                },
                "worst": {
                  "global_sensor_index": 3,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.07055141776800156,
                  "candidate": 0.06988158077001572
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.4762499788776,
            "full": 5197.372250026092
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 230.2953329635784,
            "full": 5326.77641697228
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 223.0178330792114,
            "full": 5206.838041078299
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 221.46849997807294,
            "full": 5237.124583916739
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2683.4541659336537,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-teaching-climate-phoenix/teaching_reflectance70/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10119.49387495406,
      "worker_pool_size": 12,
      "invocation_count": 3
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      36,
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
        "identifier": "teaching_reflectance70_grid",
        "full_identifier": "teaching_reflectance70_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02378047665416078,
            "cvrmse_percent": 1.8290380132808248,
            "rms_normalized_rmse_percent": 0.42864678470509865,
            "reference_energy": 8.950874704563375,
            "candidate_energy": 8.948746143893914,
            "relative_energy_error_percent": 0.023780476654160783,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1059455573558807e-07,
              "p99": 8.547503966838121e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -2.1291685175173374,
            "cvrmse_percent": 41.21468140001583,
            "rms_normalized_rmse_percent": 2.696825867798767,
            "reference_energy": 11.941502836061368,
            "candidate_energy": 11.687248117157509,
            "relative_energy_error_percent": 2.129168517517338,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2241675051427592e-07,
              "p90": 2.6039560907520357e-05,
              "p95": 3.90585046261549e-05,
              "p99": 7.196294609457254e-05,
              "maximum": 0.0027346760034561157
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07799339294433594,
              "candidate": 0.07525871694087982,
              "position": [
                1.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -1.227161815713837,
            "cvrmse_percent": 23.553357348949657,
            "rms_normalized_rmse_percent": 2.696389694486764,
            "reference_energy": 20.892377540624743,
            "candidate_energy": 20.635994261051422,
            "relative_energy_error_percent": 1.2271618157138373,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.2241675051427592e-07,
              "p90": 2.5908336101565514e-05,
              "p95": 3.8790516555309296e-05,
              "p99": 7.15556088835001e-05,
              "maximum": 0.0027346760034561157
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.07799339294433594,
              "candidate": 0.07525871694087982,
              "position": [
                1.5,
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
        "identifier": "teaching_reflectance70_grid",
        "full_identifier": "teaching_reflectance70_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02378047665416078,
            "cvrmse_percent": 1.8290380132808248,
            "rms_normalized_rmse_percent": 0.42864678470509865,
            "reference_energy": 8.950874704563375,
            "candidate_energy": 8.948746143893914,
            "relative_energy_error_percent": 0.023780476654160783,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.1059455573558807e-07,
              "p99": 8.547503966838121e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                0.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 169.6478630279287,
            "cvrmse_percent": 1887.936406033903,
            "rms_normalized_rmse_percent": 80.32948142013255,
            "reference_energy": 4.334263207547469,
            "candidate_energy": 11.687248117157509,
            "relative_energy_error_percent": 169.6478630279287,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022288699838100004,
              "p95": 0.00029120000544935465,
              "p99": 0.00042510288767516613,
              "maximum": 0.03480033203959465
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03340144082903862,
              "candidate": 0.06820177286863327,
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
            "nmbe_percent": 55.331426723387445,
            "cvrmse_percent": 615.9335092198494,
            "rms_normalized_rmse_percent": 80.32897400476975,
            "reference_energy": 13.285137912110844,
            "candidate_energy": 20.635994261051422,
            "relative_energy_error_percent": 55.33142672338745,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022312599903671107,
              "p95": 0.00029067460855003446,
              "p99": 0.0004235243541188538,
              "maximum": 0.03480033203959465
            },
            "worst": {
              "global_sensor_index": 33,
              "local_sensor_index": 33,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.03340144082903862,
              "candidate": 0.06820177286863327,
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
      "bias_percent": -0.5048692369993133,
      "rms_normalized_error_percent": 0.4282873936236255,
      "absolute_error": {
        "p95": 0.19944911488825046,
        "p99": 0.24807580806503013,
        "maximum": 0.2722306376414654
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 22.524280298142187,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.4282873936236255
    },
    "overcast": {
      "bias_percent": -0.4804151174393653,
      "rms_normalized_error_percent": 0.36815255384842727,
      "absolute_error": {
        "p95": 0.12314140796661377,
        "p99": 0.14632201194763178,
        "maximum": 0.15848016738891602
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 14.206151008605957,
      "reference_fraction_of_uniform": 0.630703866481781,
      "rms_normalized_to_uniform_percent": 0.25316263718286247
    },
    "horizon": {
      "bias_percent": -0.6813129283608729,
      "rms_normalized_error_percent": 1.66143811516041,
      "absolute_error": {
        "p95": 0.1002117907039759,
        "p99": 0.13573939550129913,
        "maximum": 0.13711957626790738
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.250951157819303,
      "reference_fraction_of_uniform": 0.14433096706257217,
      "rms_normalized_to_uniform_percent": 0.1762532943472608
    },
    "north": {
      "bias_percent": -68.79619673495502,
      "rms_normalized_error_percent": 97.46604588582925,
      "absolute_error": {
        "p95": 0.0001193404507375817,
        "p99": 0.00023010524637356842,
        "maximum": 0.00028847818612121046
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.9038790671620518e-05,
      "reference_fraction_of_uniform": 1.289221700062626e-06,
      "rms_normalized_to_uniform_percent": 0.00018778018245397933
    },
    "east": {
      "bias_percent": -0.6045273860365886,
      "rms_normalized_error_percent": 0.5050977338337638,
      "absolute_error": {
        "p95": 0.04910409450531006,
        "p99": 0.09042240381240836,
        "maximum": 0.11164259910583496
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.305843353271484,
      "reference_fraction_of_uniform": 0.1911645233631134,
      "rms_normalized_to_uniform_percent": 0.10777606371549908
    },
    "south": {
      "bias_percent": -0.4721901558279918,
      "rms_normalized_error_percent": 0.4614480870084893,
      "absolute_error": {
        "p95": 0.13325822353363037,
        "p99": 0.16644628047943108,
        "maximum": 0.18294048309326172
      },
      "worst_index": [
        1
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.74935531616211,
      "reference_fraction_of_uniform": 0.6992167830467224,
      "rms_normalized_to_uniform_percent": 0.30195264203199923
    },
    "west": {
      "bias_percent": -0.5050668944555922,
      "rms_normalized_error_percent": 0.4664917212703745,
      "absolute_error": {
        "p95": 0.05350014567375183,
        "p99": 0.05759235620498657,
        "maximum": 0.05972099304199219
      },
      "worst_index": [
        13
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.357706069946289,
      "reference_fraction_of_uniform": 0.19346705079078674,
      "rms_normalized_to_uniform_percent": 0.10039153769886622
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
          "nmbe_percent": -0.6383138546461026,
          "cvrmse_percent": 2.1516642707549396,
          "absolute_error_percentiles_lux": {
            "p50": 16.588531494140625,
            "p90": 96.10607910156254,
            "p95": 132.1683837890625,
            "p99": 219.88587646484376
          },
          "maximum_absolute_error_lux": 509.86328125,
          "worst": {
            "sensor_index": 10,
            "position": [
              1.5,
              1.5,
              0.75
            ],
            "hour_of_year": 995.5,
            "foton_lux": 37038.03515625,
            "radiance_lux": 37547.8984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.09279299847792978,
            "maximum_error_percentage_points": 0.33328767123286696,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.04404408068357194,
            "maximum_error_percentage_points": 0.13690087501315418,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.042465753424657526,
            "maximum_error_percentage_points": 0.1689041095890409,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.3691552511415521,
            "maximum_error_percentage_points": 1.0975342465753357,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.3789840182648398,
            "maximum_error_percentage_points": 1.1230136986301367,
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
      "maximum_error_percentage_points": 0.004931506849315426,
      "metrics": {
        "da": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.00492856378423312,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_reflectance70_grid",
            "maximum_error_percentage_points": 0.004794520547945158,
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
      "study_preparation_seconds": 0.007098625064827502,
      "weather_seconds": 0.10296325001399964,
      "metric_reduction_seconds": 0.13695720804389566,
      "write_seconds": 0.03433287504594773,
      "total_seconds": 0.27438887499738485,
      "cold_end_to_end_seconds": 0.28148750006221235,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.011159583111293614,
      "engine_upload_seconds": 0.000893292,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.08538033324293792,
      "engine_annual_reduction_seconds": 0.0015365417348220944,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.08538033324293792
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.007098625064827502,
      "weather_seconds": 0.10749058402143419,
      "metric_reduction_seconds": 0.04409520793706179,
      "write_seconds": 0.03328566695563495,
      "total_seconds": 0.18506849999539554,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18506849999539554,
      "raw_export_seconds": 0.011724249925464392,
      "engine_upload_seconds": 7.2834e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0016543749952688813,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.00928883405867964,
      "full": 0.07444458408281207
    }
  },
  "elapsed_seconds": 59.940262750023976,
  "result_class": "passed"
}
```
