# Foton report

Status: **passed**

```json
{
  "scene": "teaching_obstruction30",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_obstruction30",
    "category": "teaching",
    "question": "How does a 30 degree obstruction angle reduce sky access?",
    "interactions": [
      "multiple_bounces",
      "obstruction",
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
    "shades": 6,
    "sensors": 36,
    "floor_area": 36.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "65d433815849d9b4b8c88ec65b1d31fd41770ec78b45f771527ae685571f46a9",
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
      "scene_fingerprint": 16536123132161339720,
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
      "scene_fingerprint": 16536123132161339720,
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
    "maximum_samples": 16384,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "direct_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "teaching_obstruction30_grid",
        "bias_percent": -0.010951538814090998,
        "rms_normalized_error_percent": 1.075267804205868,
        "absolute_error": {
          "p95": 0.0,
          "p99": 1.6659963876008987e-05,
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
        "identifier": "teaching_obstruction30_grid",
        "bias_percent": 0.08732480670947507,
        "rms_normalized_error_percent": 1.1033158143573836,
        "absolute_error": {
          "p95": 1.8583588826004416e-05,
          "p99": 7.373990956693888e-05,
          "maximum": 0.0005325116217136383
        },
        "worst_index": [
          16,
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
        "identifier": "teaching_obstruction30_grid",
        "bias_percent": -0.007610666711445886,
        "rms_normalized_error_percent": 0.8724370057962827,
        "absolute_error": {
          "p95": 1.5597073797835037e-05,
          "p99": 6.0063088312745094e-05,
          "maximum": 0.000453021377325058
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
          "rms_normalized_rmse_percent": 10.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.048975965511611944,
                "cvrmse_percent": 48.784101692425,
                "rms_normalized_rmse_percent": 7.789952450184777,
                "reference_energy": 5.063814353537964,
                "candidate_energy": 5.066294405509325,
                "relative_energy_error_percent": 0.04897596551161194,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00020746502559632063,
                  "maximum": 0.0007103988900780678
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 359,
                  "rgb_channel": 0,
                  "reference": 0.004443347919732332,
                  "candidate": 0.0037329490296542645
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.009296209861583467,
                "cvrmse_percent": 99.26428729680106,
                "rms_normalized_rmse_percent": 4.015806201361116,
                "reference_energy": 3.19869032896181,
                "candidate_energy": 3.1989876859276123,
                "relative_energy_error_percent": 0.009296209861583467,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.8653729603101966e-05,
                  "p95": 3.682917849801015e-05,
                  "p99": 0.00026847037952393293,
                  "maximum": 0.0009204259840771556
                },
                "worst": {
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "sky_patch_index": 358,
                  "rgb_channel": 0,
                  "reference": 0.0003081149188801646,
                  "candidate": -0.000612311065196991
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
              "20000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 125.19795901607722,
            "full": 234.56516698934138
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 111.63575004320592,
            "full": 234.23662490677088
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.62462504766881,
            "full": 225.65662499982864
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 115.6234999652952,
            "full": 230.23783403914422
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
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.00502966953109675,
                "cvrmse_percent": 22.2815728989834,
                "rms_normalized_rmse_percent": 3.5691692550122145,
                "reference_energy": 5.07155234077436,
                "candidate_energy": 5.071807423097198,
                "relative_energy_error_percent": 0.00502966953109675,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00010745157487690449,
                  "maximum": 0.00030416890513151884
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 258,
                  "rgb_channel": 0,
                  "reference": 0.002770003047771752,
                  "candidate": 0.0030741719529032707
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.09098395516154373,
                "cvrmse_percent": 35.83008571183262,
                "rms_normalized_rmse_percent": 1.8057730318138365,
                "reference_energy": 5.087075222047602,
                "candidate_energy": 5.08244679980854,
                "relative_energy_error_percent": 0.09098395516154373,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.249896735724178e-06,
                  "p90": 1.7044510605046534e-05,
                  "p95": 2.6917994546238333e-05,
                  "p99": 0.00014697050210088491,
                  "maximum": 0.0007379837334156036
                },
                "worst": {
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.051404185593128204,
                  "candidate": 0.05214216932654381
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 149.26591597031802,
            "full": 2239.8266670061275
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 148.4849590342492,
            "full": 2237.7424580045044
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 145.94716706778854,
            "full": 2291.428458993323
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 159.44633400067687,
            "full": 2241.0632909741253
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
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.17205887539437298,
                "cvrmse_percent": 22.397762511168917,
                "rms_normalized_rmse_percent": 3.58467055654599,
                "reference_energy": 5.07374803291259,
                "candidate_energy": 5.065018199106817,
                "relative_energy_error_percent": 0.17205887539437298,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 9.052245877683163e-05,
                  "maximum": 0.00042901153210550547
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 312,
                  "rgb_channel": 0,
                  "reference": 0.0035070599988102913,
                  "candidate": 0.003078048466704786
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.10415972516617514,
                "cvrmse_percent": 37.72911266334058,
                "rms_normalized_rmse_percent": 1.8987692469690456,
                "reference_energy": 5.0932742089947745,
                "candidate_energy": 5.098579349412823,
                "relative_energy_error_percent": 0.10415972516617512,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.3366739558005065e-06,
                  "p90": 1.6998153841996128e-05,
                  "p95": 2.7424686777521856e-05,
                  "p99": 0.00014731221017427742,
                  "maximum": 0.0008276794105768204
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03533266484737396,
                  "candidate": 0.03450498543679714
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 154.89754092413932,
            "full": 2350.13495804742
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 144.2190840607509,
            "full": 2418.66770805791
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 141.4977500680834,
            "full": 2405.5319590261206
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 157.47179195750505,
            "full": 2361.05312500149
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
            "identifier": "teaching_obstruction30_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.007111255886672372,
                "cvrmse_percent": 11.64565229777435,
                "rms_normalized_rmse_percent": 1.8643557641694137,
                "reference_energy": 5.070393498026988,
                "candidate_energy": 5.070754066683094,
                "relative_energy_error_percent": 0.007111255886672372,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 5.249795503914356e-05,
                  "maximum": 0.0001923911040648818
                },
                "worst": {
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "sky_patch_index": 357,
                  "rgb_channel": 0,
                  "reference": 0.0037318789400160313,
                  "candidate": 0.003924270044080913
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.005673947846715305,
                "cvrmse_percent": 22.163698921613406,
                "rms_normalized_rmse_percent": 1.1173408249975827,
                "reference_energy": 5.094106961375875,
                "candidate_energy": 5.093817924403631,
                "relative_energy_error_percent": 0.005673947846715304,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.30541104428994e-06,
                  "p90": 1.1984902175754546e-05,
                  "p95": 1.8839047697838396e-05,
                  "p99": 8.34236852824688e-05,
                  "maximum": 0.0006172303110361099
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04773737117648125,
                  "candidate": 0.04712014086544514
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
              "80000",
              "-lw",
              "1e-7",
              "-dr",
              "0",
              "-n",
              "12",
              "-",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 222.237000009045,
            "full": 4128.481624997221
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 219.5360839832574,
            "full": 4232.966542011127
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 214.80762492865324,
            "full": 4189.470291952603
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 218.23820797726512,
            "full": 4139.83920798637
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2751.6317080007866,
      "worker_pool_size": 12,
      "invocation_count": 3
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal/teaching_obstruction30/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 11210.906874970533,
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
        "identifier": "teaching_obstruction30_grid",
        "full_identifier": "teaching_obstruction30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.06832441174994729,
            "cvrmse_percent": 3.7945560447423836,
            "rms_normalized_rmse_percent": 0.6076548894438821,
            "reference_energy": 5.070620199690893,
            "candidate_energy": 5.06715572826738,
            "relative_energy_error_percent": 0.06832441174994729,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 9.590876288712025e-06,
              "maximum": 8.184730540961027e-05
            },
            "worst": {
              "global_sensor_index": 27,
              "local_sensor_index": 27,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0010064404923468828,
              "candidate": 0.0009245931869372725,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1463054751077313,
            "cvrmse_percent": 56.10912192442251,
            "rms_normalized_rmse_percent": 2.8280923568761263,
            "reference_energy": 5.093916088919634,
            "candidate_energy": 5.035524249894955,
            "relative_energy_error_percent": 1.146305475107731,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 7.55246128392173e-06,
              "p90": 3.1843370891238017e-05,
              "p95": 4.426072655405733e-05,
              "p99": 8.019243978196755e-05,
              "maximum": 0.002056114375591278
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.049227144569158554,
              "candidate": 0.047171030193567276,
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
            "nmbe_percent": -0.6085502446137444,
            "cvrmse_percent": 28.09555873658072,
            "rms_normalized_rmse_percent": 2.825748938809445,
            "reference_energy": 10.164536288610527,
            "candidate_energy": 10.102679978162335,
            "relative_energy_error_percent": 0.6085502446137443,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 7.54584880269249e-06,
              "p90": 3.1767738431654036e-05,
              "p95": 4.425639781402424e-05,
              "p99": 7.837405428290367e-05,
              "maximum": 0.002056114375591278
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.049227144569158554,
              "candidate": 0.047171030193567276,
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
        "identifier": "teaching_obstruction30_grid",
        "full_identifier": "teaching_obstruction30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.06832441174994729,
            "cvrmse_percent": 3.7945560447423836,
            "rms_normalized_rmse_percent": 0.6076548894438821,
            "reference_energy": 5.070620199690893,
            "candidate_energy": 5.06715572826738,
            "relative_energy_error_percent": 0.06832441174994729,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 0.0,
              "p99": 9.590876288712025e-06,
              "maximum": 8.184730540961027e-05
            },
            "worst": {
              "global_sensor_index": 27,
              "local_sensor_index": 27,
              "sky_patch_index": 265,
              "rgb_channel": 0,
              "reference": 0.0010064404923468828,
              "candidate": 0.0009245931869372725,
              "position": [
                4.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 57.691621549816034,
            "cvrmse_percent": 764.5853366864353,
            "rms_normalized_rmse_percent": 30.872427981366062,
            "reference_energy": 3.1932731748238083,
            "candidate_energy": 5.035524249894955,
            "relative_energy_error_percent": 57.69162154981603,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 6.839350817244849e-06,
              "p90": 5.237000004854053e-05,
              "p95": 8.022999827517197e-05,
              "p99": 0.00016377517022192478,
              "maximum": 0.012229133397340775
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017976656556129456,
              "candidate": 0.03020578995347023,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 22.250851025236237,
            "cvrmse_percent": 295.4382015510508,
            "rms_normalized_rmse_percent": 30.871668677772963,
            "reference_energy": 8.263893374514701,
            "candidate_energy": 10.102679978162335,
            "relative_energy_error_percent": 22.250851025236237,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 6.859999757580226e-06,
              "p90": 5.233155061432638e-05,
              "p95": 8.010298734006938e-05,
              "p99": 0.00016446516383439302,
              "maximum": 0.012229133397340775
            },
            "worst": {
              "global_sensor_index": 2,
              "local_sensor_index": 2,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.017976656556129456,
              "candidate": 0.03020578995347023,
              "position": [
                0.5,
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
      "bias_percent": -0.07591613003760667,
      "rms_normalized_error_percent": 0.3904757975192184,
      "absolute_error": {
        "p95": 0.14362200155180993,
        "p99": 0.15581889697719295,
        "maximum": 0.16222599768541812
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 10.544442950309705,
      "rms_normalized_to_uniform_percent": 0.3904757975192184
    },
    "overcast": {
      "bias_percent": -0.054217706091938656,
      "rms_normalized_error_percent": 0.3874872496735234,
      "absolute_error": {
        "p95": 0.11253762245178223,
        "p99": 0.13404393196105954,
        "maximum": 0.14108848571777344
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 7.816649436950684,
      "rms_normalized_to_uniform_percent": 0.2999645726743893
    },
    "horizon": {
      "bias_percent": -0.45079919993443796,
      "rms_normalized_error_percent": 6.742419045285497,
      "absolute_error": {
        "p95": 0.05697496314452716,
        "p99": 0.06416878794842326,
        "maximum": 0.06469619494796341
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.32098693284253876,
      "rms_normalized_to_uniform_percent": 0.13010157294073652
    },
    "north": {
      "bias_percent": -0.31333570253295273,
      "rms_normalized_error_percent": 2.3968044020479553,
      "absolute_error": {
        "p95": 0.030185677111148834,
        "p99": 0.03674333542585372,
        "maximum": 0.03919786214828491
      },
      "worst_index": [
        15
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 0.6005287766456604,
      "rms_normalized_to_uniform_percent": 0.08136599064329901
    },
    "east": {
      "bias_percent": -0.18715671169701606,
      "rms_normalized_error_percent": 0.723676153806134,
      "absolute_error": {
        "p95": 0.06489908695220947,
        "p99": 0.08553035259246825,
        "maximum": 0.09035539627075195
      },
      "worst_index": [
        4
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.100435733795166,
      "rms_normalized_to_uniform_percent": 0.15558171800913215
    },
    "south": {
      "bias_percent": -0.05480829436971443,
      "rms_normalized_error_percent": 0.38581178701518776,
      "absolute_error": {
        "p95": 0.07426368445158005,
        "p99": 0.10088608264923092,
        "maximum": 0.11006736755371094
      },
      "worst_index": [
        22
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 5.4735870361328125,
      "rms_normalized_to_uniform_percent": 0.20203306558664755
    },
    "west": {
      "bias_percent": -0.07989024015591498,
      "rms_normalized_error_percent": 0.5597305366468383,
      "absolute_error": {
        "p95": 0.04631718248128891,
        "p99": 0.04866714477539062,
        "maximum": 0.048956871032714844
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "reference_mean": 2.1077542304992676,
      "rms_normalized_to_uniform_percent": 0.12080642893114162
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
        "identifier": "teaching_obstruction30_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.13537517793372061,
          "cvrmse_percent": 5.0362471705592275,
          "absolute_error_percentiles_lux": {
            "p50": 4.9690399169921875,
            "p90": 71.36592254638673,
            "p95": 113.30428009033194,
            "p99": 214.22885375976483
          },
          "maximum_absolute_error_lux": 701.7286376953125,
          "worst": {
            "sensor_index": 19,
            "position": [
              3.5,
              4.5,
              0.75
            ],
            "hour_of_year": 5748.5,
            "foton_lux": 1452.30810546875,
            "radiance_lux": 750.5794677734375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.9103424657534257,
            "maximum_error_percentage_points": 3.6213698630136975,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.6004017414926839,
            "maximum_error_percentage_points": 2.0531213678943985,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.5087176560121764,
            "maximum_error_percentage_points": 3.0980821917808257,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.517800608828006,
            "maximum_error_percentage_points": 3.0980821917808257,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.02760273972602746,
            "maximum_error_percentage_points": 0.1376712328767118,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 25.0,
          "radiance_percent": 25.0,
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
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849313649,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004804687499998295,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_obstruction30_grid",
            "maximum_error_percentage_points": 0.00479452054794538,
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
      "study_preparation_seconds": 0.012942957924678922,
      "weather_seconds": 0.11272104200907052,
      "metric_reduction_seconds": 0.06677383393980563,
      "write_seconds": 0.03568012500181794,
      "total_seconds": 0.21573095896746963,
      "cold_end_to_end_seconds": 0.22867391689214855,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.013478207984007895,
      "engine_upload_seconds": 0.000805833,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.017146999831311405,
      "engine_annual_reduction_seconds": 0.0015453749801963568,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.017146999831311405
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.012942957924678922,
      "weather_seconds": 0.11261204199399799,
      "metric_reduction_seconds": 0.043472624965943396,
      "write_seconds": 0.024247624911367893,
      "total_seconds": 0.18048774998169392,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.18048774998169392,
      "raw_export_seconds": 0.011121709016151726,
      "engine_upload_seconds": 0.000382792,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0015410000924021006,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013966707978397608,
      "full": 0.01403895893599838
    }
  },
  "elapsed_seconds": 54.968183249933645,
  "result_class": "passed"
}
```
