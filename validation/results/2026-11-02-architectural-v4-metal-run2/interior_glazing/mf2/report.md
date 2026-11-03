# Foton report

Status: **incomplete**

```json
{
  "scene": "interior_glazing",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "interior_glazing",
    "category": "connections",
    "question": "Does daylight pass through a shared glazed wall exactly once?",
    "interactions": [
      "borrowed_light",
      "paired_apertures",
      "room_isolation"
    ],
    "room_count": 2,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 2,
    "apertures": 3,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 8.999999999999996
  },
  "sky_density": 2,
  "status": "incomplete",
  "passed": false,
  "model_sha256": "af65586b86a7343b6dbb02eb2bd7490480c9aaaf810cb68c4f0db396a505f09c",
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
      "scene_fingerprint": 14976319759523577797,
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
      "scene_fingerprint": 14976319759523577797,
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
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": -0.02630459349567195,
        "rms_normalized_error_percent": 0.7598521188292517,
        "absolute_error": {
          "p95": 4.362664185464382e-08,
          "p99": 7.011898560449481e-06,
          "maximum": 0.00014028436271473765
        },
        "worst_index": [
          17,
          543,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": 0.0434975018413777,
        "rms_normalized_error_percent": 2.2008082752797096,
        "absolute_error": {
          "p95": 0.0,
          "p99": 0.0,
          "maximum": 2.3427215637639165e-05
        },
        "worst_index": [
          7,
          157,
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
    "passed": false,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": 0.09175882332940995,
        "rms_normalized_error_percent": 1.7659514676644854,
        "absolute_error": {
          "p95": 1.9649742171168327e-05,
          "p99": 0.00010204059071838856,
          "maximum": 0.0004292801022529602
        },
        "worst_index": [
          22,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": 1.0941130045286585,
        "rms_normalized_error_percent": 5.182081192771644,
        "absolute_error": {
          "p95": 2.2243023067858303e-06,
          "p99": 6.004513920743193e-06,
          "maximum": 0.00011277434532530606
        },
        "worst_index": [
          12,
          38,
          0
        ],
        "passed": false
      }
    ]
  },
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "interior_glazing_grid",
        "bias_percent": -0.028330842085558347,
        "rms_normalized_error_percent": 1.4916696260467257,
        "absolute_error": {
          "p95": 1.7428974388167262e-05,
          "p99": 8.361181244254112e-05,
          "maximum": 0.00044220685958862305
        },
        "worst_index": [
          28,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "adjacent_grid",
        "bias_percent": -0.8995957026230028,
        "rms_normalized_error_percent": 4.8341345145084675,
        "absolute_error": {
          "p95": 1.910268110805191e-06,
          "p99": 5.104176693748741e-06,
          "maximum": 0.00021984614431858063
        },
        "worst_index": [
          2,
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
        "run_count": 8,
        "half_run_count": 4,
        "oracle_stable": true,
        "gates": {
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.051915994187959,
                "cvrmse_percent": 39.71388462781514,
                "rms_normalized_rmse_percent": 7.651060950264262,
                "reference_energy": 6.0232257529402204,
                "candidate_energy": 6.0263527704720445,
                "relative_energy_error_percent": 0.051915994187958996,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.025426460430026e-05,
                  "p99": 0.0002088567998725921,
                  "maximum": 0.0006526650977320969
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 209,
                  "rgb_channel": 0,
                  "reference": 0.0019569455762393773,
                  "candidate": 0.0013042804785072803
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.3961444350542931,
                "cvrmse_percent": 160.72456129671465,
                "rms_normalized_rmse_percent": 5.903449830646009,
                "reference_energy": 2.009625782919823,
                "candidate_energy": 2.017586803624276,
                "relative_energy_error_percent": 0.39614443505429314,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.501554340346047e-06,
                  "p95": 4.4981250539422035e-05,
                  "p99": 0.00028412273968569934,
                  "maximum": 0.0010709292255342007
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.017846439965069294,
                  "candidate": 0.016775510739535093
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.49093036378209726,
                "cvrmse_percent": 454.785414274501,
                "rms_normalized_rmse_percent": 21.639758327782182,
                "reference_energy": 0.06450307715931558,
                "candidate_energy": 0.06481974235066446,
                "relative_energy_error_percent": 0.49093036378209737,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0002440009902784368
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 39,
                  "rgb_channel": 0,
                  "reference": 0.0002685149447643198,
                  "candidate": 2.4513954485883005e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.015802413004514584,
                "cvrmse_percent": 626.8408585435502,
                "rms_normalized_rmse_percent": 16.950652605168948,
                "reference_energy": 0.06995186990840807,
                "candidate_energy": 0.06994081582502076,
                "relative_energy_error_percent": 0.015802413004514584,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 4.623284439730924e-06,
                  "maximum": 0.0003433243346080417
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 39,
                  "rgb_channel": 0,
                  "reference": -0.00012510566193668637,
                  "candidate": 0.0002182186726713553
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 133.94549989607185,
            "full": 381.3874999759719
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 123.85454098694026,
            "full": 375.22054195869714
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.69850001111627,
            "full": 390.08129201829433
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 130.88149996474385,
            "full": 388.88850004877895
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 127.1432910580188,
            "full": 381.7277089692652
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 126.47570902481675,
            "full": 377.0613329252228
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 123.40475001838058,
            "full": 385.8281249413267
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 130.21237507928163,
            "full": 387.0169169967994
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.017990096768779752,
                "cvrmse_percent": 23.48469745504997,
                "rms_normalized_rmse_percent": 4.529499719964379,
                "reference_energy": 6.02056609400131,
                "candidate_energy": 6.0216491996676496,
                "relative_energy_error_percent": 0.017990096768779752,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2687148884870112e-05,
                  "p99": 0.00012715088087134063,
                  "maximum": 0.0003028789651580155
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 149,
                  "rgb_channel": 0,
                  "reference": 0.0016537500196136534,
                  "candidate": 0.001956628984771669
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.039445691143265176,
                "cvrmse_percent": 61.58339807685929,
                "rms_normalized_rmse_percent": 3.2237865914946195,
                "reference_energy": 3.6216929688573174,
                "candidate_energy": 3.6202643670346646,
                "relative_energy_error_percent": 0.039445691143265176,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.9446014576374182e-08,
                  "p90": 1.2858454465458635e-05,
                  "p95": 3.482046304270625e-05,
                  "p99": 0.0001937664346769452,
                  "maximum": 0.0008065942674875259
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.028082880191504955,
                  "candidate": 0.02888947445899248
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -1.0194631455531373,
                "cvrmse_percent": 318.4604335983058,
                "rms_normalized_rmse_percent": 15.12934820961407,
                "reference_energy": 0.06436909272633784,
                "candidate_energy": 0.0637128735488659,
                "relative_energy_error_percent": 1.0194631455531373,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.00014502013800665736
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 8,
                  "sky_patch_index": 99,
                  "rgb_channel": 0,
                  "reference": 0.000591285788686946,
                  "candidate": 0.00044626565068028867
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.1608877574796495,
                "cvrmse_percent": 198.73265761932404,
                "rms_normalized_rmse_percent": 9.287712722142459,
                "reference_energy": 0.1657372507711301,
                "candidate_energy": 0.1676612742249155,
                "relative_energy_error_percent": 1.1608877574796492,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7252901812980807e-06,
                  "p95": 3.185894001944689e-06,
                  "p99": 8.873125352693023e-06,
                  "maximum": 0.0002331503201276064
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.004037067526951432,
                  "candidate": 0.004270217847079039
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.25620799139142,
            "full": 5029.329249984585
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 189.2938339151442,
            "full": 4990.441458066925
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 184.24008297733963,
            "full": 5052.35008301679
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.8898329557851,
            "full": 5017.608791938983
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08467436645662962,
                "cvrmse_percent": 25.080352632334485,
                "rms_normalized_rmse_percent": 4.845095968366463,
                "reference_energy": 6.026835356327183,
                "candidate_energy": 6.021732171671829,
                "relative_energy_error_percent": 0.08467436645662961,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2579682990908623e-05,
                  "p99": 0.00013798440340906382,
                  "maximum": 0.00031751347705721855
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 271,
                  "rgb_channel": 0,
                  "reference": 0.0029780310578644276,
                  "candidate": 0.003295544534921646
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.07541341408573646,
                "cvrmse_percent": 63.314805076479296,
                "rms_normalized_rmse_percent": 3.3117651318653794,
                "reference_energy": 3.625283057231421,
                "candidate_energy": 3.628017006955151,
                "relative_energy_error_percent": 0.07541341408573647,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.1714986314359521e-08,
                  "p90": 1.291502678668622e-05,
                  "p95": 3.676704363897443e-05,
                  "p99": 0.00019414897542446852,
                  "maximum": 0.0007298300042748451
                },
                "worst": {
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.02010447531938553,
                  "candidate": 0.020834305323660374
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 3.2399651368390163,
                "cvrmse_percent": 306.9624122140843,
                "rms_normalized_rmse_percent": 14.430664787550967,
                "reference_energy": 0.06343549822577188,
                "candidate_energy": 0.06549078625266702,
                "relative_energy_error_percent": 3.2399651368390154,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 0.0001571416505612433
                },
                "worst": {
                  "global_sensor_index": 42,
                  "local_sensor_index": 6,
                  "sky_patch_index": 98,
                  "rgb_channel": 0,
                  "reference": 0.0004222348507028073,
                  "candidate": 0.0005793765012640506
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -2.06276285410722,
                "cvrmse_percent": 178.06609645406672,
                "rms_normalized_rmse_percent": 8.373356292306426,
                "reference_energy": 0.17056079477564623,
                "candidate_energy": 0.16704253005734415,
                "relative_energy_error_percent": 2.0627628541072194,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.7680213993287494e-06,
                  "p95": 3.1378551170746505e-06,
                  "p99": 9.466325309404056e-06,
                  "maximum": 0.00015187474491540343
                },
                "worst": {
                  "global_sensor_index": 42,
                  "local_sensor_index": 6,
                  "sky_patch_index": 98,
                  "rgb_channel": 0,
                  "reference": 7.46091827750206e-05,
                  "candidate": -7.726556214038283e-05
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 191.59337505698204,
            "full": 5316.693332977593
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 186.22462498024106,
            "full": 5339.952541980892
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 191.28795806318521,
            "full": 5317.565709003247
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 188.52199998218566,
            "full": 5321.811917005107
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
            "identifier": "interior_glazing_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.04061632123695413,
                "cvrmse_percent": 13.951561191316383,
                "rms_normalized_rmse_percent": 2.6947832593530574,
                "reference_energy": 6.024297780195241,
                "candidate_energy": 6.026744628333915,
                "relative_energy_error_percent": 0.04061632123695412,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1721494956873357e-05,
                  "p99": 7.743043533992022e-05,
                  "maximum": 0.00017517595551908016
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 151,
                  "rgb_channel": 0,
                  "reference": 0.001857410476077348,
                  "candidate": 0.0016822345205582678
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.2203305092130117,
                "cvrmse_percent": 35.970161277286344,
                "rms_normalized_rmse_percent": 1.8859326028853831,
                "reference_energy": 3.6266737312958597,
                "candidate_energy": 3.618683062596201,
                "relative_energy_error_percent": 0.22033050921301167,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.4540800563622724e-08,
                  "p90": 8.939598319557294e-06,
                  "p95": 2.1239451598376036e-05,
                  "p99": 0.00011077895760536194,
                  "maximum": 0.0006954539567232132
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.033154940232634544,
                  "candidate": 0.03385039418935776
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "adjacent_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -1.3204005532685459,
                "cvrmse_percent": 129.98460272734553,
                "rms_normalized_rmse_percent": 6.249954182720408,
                "reference_energy": 0.06438489419088,
                "candidate_energy": 0.06353475569176226,
                "relative_energy_error_percent": 1.3204005532685459,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.0,
                  "maximum": 4.800349415745586e-05
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 7,
                  "sky_patch_index": 159,
                  "rgb_channel": 0,
                  "reference": 0.0001079861649486702,
                  "candidate": 5.998267079121433e-05
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 1.8682099387201856,
                "cvrmse_percent": 122.32164520700914,
                "rms_normalized_rmse_percent": 5.790512054141813,
                "reference_energy": 0.1656591097200284,
                "candidate_energy": 0.16875396967221334,
                "relative_energy_error_percent": 1.8682099387201856,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2558404350215828e-06,
                  "p95": 2.189166082189331e-06,
                  "p99": 5.936952902629855e-06,
                  "maximum": 0.00025767553597688675
                },
                "worst": {
                  "global_sensor_index": 39,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.003967304015532136,
                  "candidate": 0.004224979551509023
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 306.47437495645136,
            "full": 9347.542708041146
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 304.25241601187736,
            "full": 9581.814291072078
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 302.5999589590356,
            "full": 9275.622666929848
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 306.3288750126958,
            "full": 9423.261250020005
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 10714.524749899283,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/interior_glazing/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 42621.67870893609,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16948668053065924,
            "cvrmse_percent": 3.731919546018636,
            "rms_normalized_rmse_percent": 0.7209215703511979,
            "reference_energy": 6.02483990591449,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.16948668053065924,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.3818650990724564e-08,
              "p99": 9.110369319387246e-06,
              "maximum": 0.00011773567530326545
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 144,
              "rgb_channel": 0,
              "reference": 0.00011773567530326545,
              "candidate": 0.0,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.027494926488274,
            "cvrmse_percent": 43.57664764266188,
            "rms_normalized_rmse_percent": 2.282329783551997,
            "reference_energy": 3.6233596967223907,
            "candidate_energy": 3.586129859670147,
            "relative_energy_error_percent": 1.027494926488274,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 1.0112455856869948e-05,
              "p95": 1.692422665655613e-05,
              "p99": 5.10878162458539e-05,
              "maximum": 0.0010368824005126953
            },
            "worst": {
              "global_sensor_index": 27,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026774821802973747,
              "candidate": 0.025737939402461052,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.49170975073005996,
            "cvrmse_percent": 16.238617937637212,
            "rms_normalized_rmse_percent": 2.264688501112912,
            "reference_energy": 9.64819960263688,
            "candidate_energy": 9.600758464420815,
            "relative_energy_error_percent": 0.4917097507300691,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.5000000292152436e-08,
              "p90": 9.961337218555856e-06,
              "p95": 1.647835597395897e-05,
              "p99": 4.732096567749977e-05,
              "maximum": 0.0010368824005126953
            },
            "worst": {
              "global_sensor_index": 27,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.026774821802973747,
              "candidate": 0.025737939402461052,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "adjacent_grid",
        "full_identifier": "adjacent_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.023336678575401514,
            "cvrmse_percent": 21.956772502759733,
            "rms_normalized_rmse_percent": 1.0529825003765718,
            "reference_energy": 0.06414209702461449,
            "candidate_energy": 0.06412712838960033,
            "relative_energy_error_percent": 0.023336678575401514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.1447817087173462e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 159,
              "rgb_channel": 0,
              "reference": 0.0005599533906206489,
              "candidate": 0.0005485055735334754,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.09477512024206537,
            "cvrmse_percent": 74.07118219698128,
            "rms_normalized_rmse_percent": 3.4999360075145733,
            "reference_energy": 0.16702426760320854,
            "candidate_energy": 0.16686597015275417,
            "relative_energy_error_percent": 0.09477512024206537,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.342332544140847e-06,
              "p95": 2.158955339837121e-06,
              "p99": 4.8097322178364266e-06,
              "maximum": 0.00012779305689036846
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.003679777029901743,
              "candidate": 0.0038075700867921114,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.0749529827782187,
            "cvrmse_percent": 53.41310768013655,
            "rms_normalized_rmse_percent": 3.49304146974915,
            "reference_energy": 0.23116636462782303,
            "candidate_energy": 0.2309930985423545,
            "relative_energy_error_percent": 0.07495298277821869,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.344876940834184e-06,
              "p95": 2.1685214619537874e-06,
              "p99": 4.792120307683945e-06,
              "maximum": 0.00012779305689036846
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.003679777029901743,
              "candidate": 0.0038075700867921114,
              "position": [
                6.5,
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
        "identifier": "interior_glazing_grid",
        "full_identifier": "interior_glazing_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16948668053065924,
            "cvrmse_percent": 3.731919546018636,
            "rms_normalized_rmse_percent": 0.7209215703511979,
            "reference_energy": 6.02483990591449,
            "candidate_energy": 6.014628604750669,
            "relative_energy_error_percent": 0.16948668053065924,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.3818650990724564e-08,
              "p99": 9.110369319387246e-06,
              "maximum": 0.00011773567530326545
            },
            "worst": {
              "global_sensor_index": 32,
              "local_sensor_index": 32,
              "sky_patch_index": 144,
              "rgb_channel": 0,
              "reference": 0.00011773567530326545,
              "candidate": 0.0,
              "position": [
                5.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 78.0993667295174,
            "cvrmse_percent": 803.9810081853662,
            "rms_normalized_rmse_percent": 29.578408242788687,
            "reference_energy": 2.0135556490307263,
            "candidate_energy": 3.586129859670147,
            "relative_energy_error_percent": 78.0993667295174,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.3138843213673695e-05,
              "p95": 7.294822898984421e-05,
              "p99": 0.00013579311780631542,
              "maximum": 0.00742778554558754
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01567065343260765,
              "candidate": 0.02309843897819519,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.43625315271323,
            "cvrmse_percent": 201.36172348651718,
            "rms_normalized_rmse_percent": 29.57410872221389,
            "reference_energy": 8.038395554945216,
            "candidate_energy": 9.600758464420815,
            "relative_energy_error_percent": 19.43625315271322,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.2474359290499736e-05,
              "p95": 7.220152201625751e-05,
              "p99": 0.0001345369964838028,
              "maximum": 0.00742778554558754
            },
            "worst": {
              "global_sensor_index": 3,
              "local_sensor_index": 3,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01567065343260765,
              "candidate": 0.02309843897819519,
              "position": [
                0.5,
                2.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "adjacent_grid",
        "full_identifier": "adjacent_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.023336678575401514,
            "cvrmse_percent": 21.956772502759733,
            "rms_normalized_rmse_percent": 1.0529825003765718,
            "reference_energy": 0.06414209702461449,
            "candidate_energy": 0.06412712838960033,
            "relative_energy_error_percent": 0.023336678575401514,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 0.0,
              "maximum": 1.1447817087173462e-05
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 159,
              "rgb_channel": 0,
              "reference": 0.0005599533906206489,
              "candidate": 0.0005485055735334754,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 136.8046785825641,
            "cvrmse_percent": 1683.5272209838247,
            "rms_normalized_rmse_percent": 45.88797005084411,
            "reference_energy": 0.07046565597924825,
            "candidate_energy": 0.16686597015275417,
            "relative_energy_error_percent": 136.80467858256407,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.686354287106991e-06,
              "p95": 4.779999926540768e-06,
              "p99": 1.3719999515160453e-05,
              "maximum": 0.001268736319616437
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0025388337671756744,
              "candidate": 0.0038075700867921114,
              "position": [
                6.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 71.60460180605337,
            "cvrmse_percent": 881.2590739743523,
            "rms_normalized_rmse_percent": 45.885437885625315,
            "reference_energy": 0.13460775300386274,
            "candidate_energy": 0.2309930985423545,
            "relative_energy_error_percent": 71.60460180605337,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 2.687000005607886e-06,
              "p95": 4.779999926540768e-06,
              "p99": 1.3670000043930486e-05,
              "maximum": 0.001268736319616437
            },
            "worst": {
              "global_sensor_index": 38,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.0025388337671756744,
              "candidate": 0.0038075700867921114,
              "position": [
                6.5,
                3.5,
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
      "bias_percent": 0.03292360614612597,
      "rms_normalized_error_percent": 0.1966416284521329,
      "absolute_error": {
        "p95": 0.0677231861007872,
        "p99": 0.10442129485511124,
        "maximum": 0.11157230283263475
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.044846505971432,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1966416284521329
    },
    "overcast": {
      "bias_percent": 0.006627487802094799,
      "rms_normalized_error_percent": 0.14296781409035053,
      "absolute_error": {
        "p95": 0.03719932436943055,
        "p99": 0.04741789340972908,
        "maximum": 0.05620574951171875
      },
      "worst_index": [
        32
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.865108013153076,
      "reference_fraction_of_uniform": 0.6394054889678955,
      "rms_normalized_to_uniform_percent": 0.10179025682719983
    },
    "horizon": {
      "bias_percent": 0.8108595440757265,
      "rms_normalized_error_percent": 1.7832440565087868,
      "absolute_error": {
        "p95": 0.03907553108662816,
        "p99": 0.0645637557716449,
        "maximum": 0.06954491799896356
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.7216637752648578,
      "reference_fraction_of_uniform": 0.11938496280293613,
      "rms_normalized_to_uniform_percent": 0.12093435853818386
    },
    "north": {
      "bias_percent": -93.64275971965564,
      "rms_normalized_error_percent": 98.60463234742858,
      "absolute_error": {
        "p95": 5.170638478375638e-05,
        "p99": 0.0002479117375696669,
        "maximum": 0.00034661650033740443
      },
      "worst_index": [
        21
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.2856893590651453e-05,
      "reference_fraction_of_uniform": 2.126918161593494e-06,
      "rms_normalized_to_uniform_percent": 0.0003364549386060417
    },
    "east": {
      "bias_percent": 0.001486284249192065,
      "rms_normalized_error_percent": 0.24685868566121516,
      "absolute_error": {
        "p95": 0.014734643697738652,
        "p99": 0.025120646953582876,
        "maximum": 0.03765511512756348
      },
      "worst_index": [
        5
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.138314962387085,
      "reference_fraction_of_uniform": 0.1883116364479065,
      "rms_normalized_to_uniform_percent": 0.04977152209973488
    },
    "south": {
      "bias_percent": 0.10210888926729736,
      "rms_normalized_error_percent": 0.25060605704415173,
      "absolute_error": {
        "p95": 0.052022147178649905,
        "p99": 0.08418134689331075,
        "maximum": 0.10684823989868164
      },
      "worst_index": [
        18
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.202781677246094,
      "reference_fraction_of_uniform": 0.6952669024467468,
      "rms_normalized_to_uniform_percent": 0.1636104764938298
    },
    "west": {
      "bias_percent": -0.30876701431485065,
      "rms_normalized_error_percent": 0.46334542633793985,
      "absolute_error": {
        "p95": 0.03197301030158998,
        "p99": 0.06134764552116396,
        "maximum": 0.06319403648376465
      },
      "worst_index": [
        33
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1725244522094727,
      "reference_fraction_of_uniform": 0.1939709186553955,
      "rms_normalized_to_uniform_percent": 0.09323544330338683
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
        "identifier": "interior_glazing_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.043285946393867396,
          "cvrmse_percent": 1.758676326794307,
          "absolute_error_percentiles_lux": {
            "p50": 2.1226806640625,
            "p90": 22.62088012695314,
            "p95": 35.14790649414061,
            "p99": 76.81450439453124
          },
          "maximum_absolute_error_lux": 466.7509765625,
          "worst": {
            "sensor_index": 31,
            "position": [
              5.5,
              4.5,
              0.75
            ],
            "hour_of_year": 1094.5,
            "foton_lux": 5840.57763671875,
            "radiance_lux": 6307.32861328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.3126750380517507,
            "maximum_error_percentage_points": 1.2352054794520555,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.14343056710706253,
            "maximum_error_percentage_points": 0.7819599210562131,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.11020167427701694,
            "maximum_error_percentage_points": 0.5765753424657518,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.11506849315068497,
            "maximum_error_percentage_points": 0.573287671232876,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.016430745814307687,
            "maximum_error_percentage_points": 0.057808219178085096,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 52.77777777777778,
          "radiance_percent": 52.77777777777778,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "adjacent_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.7617613085212148,
          "cvrmse_percent": 14.944237395572523,
          "absolute_error_percentiles_lux": {
            "p50": 0.22879886627197266,
            "p90": 3.0384077072143554,
            "p95": 4.760808753967269,
            "p99": 9.582130737304686
          },
          "maximum_absolute_error_lux": 76.9578857421875,
          "worst": {
            "sensor_index": 1,
            "position": [
              6.5,
              4.5,
              0.75
            ],
            "hour_of_year": 6830.5,
            "foton_lux": 1022.67626953125,
            "radiance_lux": 945.7183837890625
          },
          "physically_dark": false,
          "passed": false
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.006666666666666672,
            "maximum_error_percentage_points": 0.0595890410958904,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.09330614888910868,
            "maximum_error_percentage_points": 0.2627197741363223,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.051111111111111995,
            "maximum_error_percentage_points": 0.852876712328765,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.050966514459665206,
            "maximum_error_percentage_points": 0.8476712328767135,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0001331811263318111,
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 0.0,
          "radiance_percent": 0.0,
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
    "numerical_correctness": "incomplete",
    "honeybee_compatibility": "passed",
    "performance": "measured"
  },
  "compatibility": {
    "official_loader": {
      "passed": true,
      "tolerance_percentage_points": 0.05,
      "maximum_error_percentage_points": 0.004997190710611221,
      "metrics": {
        "da": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004835455907539199,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.004997190710611221,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004794520547953596,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "interior_glazing_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "adjacent_grid",
            "maximum_error_percentage_points": 0.0047945205479452,
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
      "study_preparation_seconds": 0.008956874953582883,
      "weather_seconds": 0.0997471249429509,
      "metric_reduction_seconds": 0.24294441600795835,
      "write_seconds": 0.04656883399002254,
      "total_seconds": 0.389438541023992,
      "cold_end_to_end_seconds": 0.3983954159775749,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.02265941700898111,
      "engine_upload_seconds": 0.000814292,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.18898008321411908,
      "engine_annual_reduction_seconds": 0.003010041662491858,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.18898008321411908
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.008956874953582883,
      "weather_seconds": 0.0996532910503447,
      "metric_reduction_seconds": 0.046934249927289784,
      "write_seconds": 0.04626316705252975,
      "total_seconds": 0.19301583303604275,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.19301583303604275,
      "raw_export_seconds": 0.017347667017020285,
      "engine_upload_seconds": 8.225e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.003035250003449619,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.012836042093113065,
      "full": 0.17785383306909353
    }
  },
  "elapsed_seconds": 142.1663793339394,
  "result_class": "unstable_reference"
}
```
