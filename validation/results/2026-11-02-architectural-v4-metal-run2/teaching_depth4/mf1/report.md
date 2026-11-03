# Foton report

Status: **passed**

```json
{
  "scene": "teaching_depth4",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_depth4",
    "category": "teaching",
    "question": "How does daylight fall off in a 4 m deep room?",
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
    "sensors": 24,
    "floor_area": 24.0,
    "aperture_area": 4.499999999999999
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "60621a01cd84980f3cc6bb1e887993fca1100d31797219ebbd315c9dedf5f158",
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
      "scene_fingerprint": 1264132388842763511,
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
      "scene_fingerprint": 1264132388842763511,
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
        "identifier": "teaching_depth4_grid",
        "bias_percent": -0.06804422780189273,
        "rms_normalized_error_percent": 0.9156604833783333,
        "absolute_error": {
          "p95": 1.6129284631460905e-05,
          "p99": 0.00015342188999056816,
          "maximum": 0.00029224716126918793
        },
        "worst_index": [
          11,
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
        "identifier": "teaching_depth4_grid",
        "bias_percent": 0.04615058559938744,
        "rms_normalized_error_percent": 0.8150048629594119,
        "absolute_error": {
          "p95": 7.546320557594299e-05,
          "p99": 0.00017976295202970505,
          "maximum": 0.0005881860852241516
        },
        "worst_index": [
          12,
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
        "identifier": "teaching_depth4_grid",
        "bias_percent": 0.004439774975913066,
        "rms_normalized_error_percent": 0.6531524635569623,
        "absolute_error": {
          "p95": 6.677350029349327e-05,
          "p99": 0.0001436285674571991,
          "maximum": 0.0004669502377510071
        },
        "worst_index": [
          1,
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0704158740945911,
                "cvrmse_percent": 13.79168817633069,
                "rms_normalized_rmse_percent": 3.9805665943540967,
                "reference_energy": 8.473682695766911,
                "candidate_energy": 8.479649513505137,
                "relative_energy_error_percent": 0.07041587409459112,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 9.269616566598415e-05,
                  "p95": 0.000283573754131794,
                  "p99": 0.0005045197904109955,
                  "maximum": 0.0008420953527092934
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.007099338807165623,
                  "candidate": 0.007941434159874916
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.007382679926329191,
                "cvrmse_percent": 58.822605399458766,
                "rms_normalized_rmse_percent": 3.972562218143107,
                "reference_energy": 2.7724749776416218,
                "candidate_energy": 2.7726796605952586,
                "relative_energy_error_percent": 0.007382679926329191,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.00012963078916072845,
                  "p95": 0.000357999000698328,
                  "p99": 0.0007393695414066315,
                  "maximum": 0.0014258152805268764
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 47,
                  "rgb_channel": 0,
                  "reference": 0.0005808812566101551,
                  "candidate": -0.0008449340239167213
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 113.27941599301994,
            "full": 194.0179169178009
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 108.84425009135157,
            "full": 198.69808305520564
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 115.85937498603016,
            "full": 184.5950409770012
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 107.34462505206466,
            "full": 185.05583296064287
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.07750426278313592,
                "cvrmse_percent": 5.829728825791451,
                "rms_normalized_rmse_percent": 1.6812178485455196,
                "reference_energy": 8.488295660269614,
                "candidate_energy": 8.48171686929527,
                "relative_energy_error_percent": 0.07750426278313592,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.640650538727641e-05,
                  "p95": 0.00010716961696743965,
                  "p99": 0.0002505197189748287,
                  "maximum": 0.0003710309974849224
                },
                "worst": {
                  "global_sensor_index": 5,
                  "local_sensor_index": 5,
                  "sky_patch_index": 45,
                  "rgb_channel": 0,
                  "reference": 0.007797714555636048,
                  "candidate": 0.007426683558151126
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.09056854778623499,
                "cvrmse_percent": 15.627037395093462,
                "rms_normalized_rmse_percent": 1.5155741208352624,
                "reference_energy": 4.926726073232523,
                "candidate_energy": 4.931188137490455,
                "relative_energy_error_percent": 0.090568547786235,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.3835021895356476e-07,
                  "p90": 6.86880957800895e-05,
                  "p95": 0.00015357777010649443,
                  "p99": 0.00035116076469421387,
                  "maximum": 0.0007627196609973907
                },
                "worst": {
                  "global_sensor_index": 1,
                  "local_sensor_index": 1,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.043573880568146706,
                  "candidate": 0.042811160907149315
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 131.62241701502353,
            "full": 1522.3924999590963
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 136.16474997252226,
            "full": 1544.2867910023779
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.28104101028293,
            "full": 1549.3899589637294
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.4233339447528,
            "full": 1528.349083964713
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.04786345852742204,
                "cvrmse_percent": 6.197477121182178,
                "rms_normalized_rmse_percent": 1.7882333233058634,
                "reference_energy": 8.487500902491774,
                "candidate_energy": 8.483438491017296,
                "relative_energy_error_percent": 0.04786345852742204,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 3.9327540434896946e-05,
                  "p95": 0.00010921260400209576,
                  "p99": 0.0002766783582046628,
                  "maximum": 0.0005313495639711618
                },
                "worst": {
                  "global_sensor_index": 15,
                  "local_sensor_index": 15,
                  "sky_patch_index": 18,
                  "rgb_channel": 0,
                  "reference": 0.0024478620616719127,
                  "candidate": 0.0019165124977007508
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.3148856446958083,
                "cvrmse_percent": 17.361831169466758,
                "rms_normalized_rmse_percent": 1.6840552986620583,
                "reference_energy": 4.926927201608173,
                "candidate_energy": 4.94244138809065,
                "relative_energy_error_percent": 0.3148856446958083,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.854727310681483e-07,
                  "p90": 7.17466464266181e-05,
                  "p95": 0.00016367225907742977,
                  "p99": 0.0004199931863695383,
                  "maximum": 0.0008290186524391174
                },
                "worst": {
                  "global_sensor_index": 9,
                  "local_sensor_index": 9,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05524275079369545,
                  "candidate": 0.05607176944613457
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 136.1737500410527,
            "full": 1637.5233330763876
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 134.87745798192918,
            "full": 1677.4139160988852
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 129.43191698286682,
            "full": 1603.3004999626428
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 135.86791697889566,
            "full": 1599.4803750654683
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
            "identifier": "teaching_depth4_grid",
            "start_sensor_index": 0,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.033176572773696296,
                "cvrmse_percent": 3.055831952457131,
                "rms_normalized_rmse_percent": 0.8814611443620171,
                "reference_energy": 8.481585381992772,
                "candidate_energy": 8.484399281339392,
                "relative_energy_error_percent": 0.033176572773696296,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.9900500774383545e-05,
                  "p95": 5.670194514095783e-05,
                  "p99": 0.00011690857354551554,
                  "maximum": 0.00022811838425695896
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 74,
                  "rgb_channel": 0,
                  "reference": 0.007338778581470251,
                  "candidate": 0.00756689696572721
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.014459242381572576,
                "cvrmse_percent": 9.590501708853754,
                "rms_normalized_rmse_percent": 0.930988045001859,
                "reference_energy": 4.938114499088378,
                "candidate_energy": 4.9374004851438755,
                "relative_energy_error_percent": 0.014459242381572576,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.599685444693023e-07,
                  "p90": 4.1435472667217255e-05,
                  "p95": 8.707819506525993e-05,
                  "p99": 0.00019569182768464088,
                  "maximum": 0.0008033700287342072
                },
                "worst": {
                  "global_sensor_index": 8,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04892929084599018,
                  "candidate": 0.048125920817255974
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
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 194.9446250218898,
            "full": 2759.192582918331
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 194.37870802357793,
            "full": 2810.22916699294
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 184.57674991805106,
            "full": 2784.778540953994
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "24",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 182.06308304797858,
            "full": 2893.0484589654952
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 481.49666690733284,
      "worker_pool_size": 12,
      "invocation_count": 2
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/teaching_depth4/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 1574.5424160268158,
      "worker_pool_size": 12,
      "invocation_count": 2
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      24,
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
        "identifier": "teaching_depth4_grid",
        "full_identifier": "teaching_depth4_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07302321444488426,
            "cvrmse_percent": 2.0812360472439875,
            "rms_normalized_rmse_percent": 0.6004414135018394,
            "reference_energy": 8.486303725720063,
            "candidate_energy": 8.480106753951986,
            "relative_energy_error_percent": 0.07302321444488426,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.476176738739014e-07,
              "p95": 1.3578683137893677e-05,
              "p99": 7.374770939350128e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
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
            "nmbe_percent": 0.031981499953866725,
            "cvrmse_percent": 12.55950048616189,
            "rms_normalized_rmse_percent": 1.2185142810675818,
            "reference_energy": 4.934446087710043,
            "candidate_energy": 4.936024197583308,
            "relative_energy_error_percent": 0.031981499953866725,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0682351785362698e-06,
              "p90": 5.231512477621436e-05,
              "p95": 8.092052303254604e-05,
              "p99": 0.00019198376685380936,
              "maximum": 0.0012303218245506287
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.051006119698286057,
              "candidate": 0.04977579787373543,
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
            "nmbe_percent": -0.03441582593388423,
            "cvrmse_percent": 4.62243056797665,
            "rms_normalized_rmse_percent": 1.2197393223697492,
            "reference_energy": 13.420749813430106,
            "candidate_energy": 13.416130951535294,
            "relative_energy_error_percent": 0.03441582593388423,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0862956969504012e-06,
              "p90": 5.129276541993022e-05,
              "p95": 7.838266901671886e-05,
              "p99": 0.0001989966258406639,
              "maximum": 0.0012303218245506287
            },
            "worst": {
              "global_sensor_index": 5,
              "local_sensor_index": 5,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.051006119698286057,
              "candidate": 0.04977579787373543,
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
      24,
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
        "identifier": "teaching_depth4_grid",
        "full_identifier": "teaching_depth4_grid",
        "start_sensor_index": 0,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.07302321444488426,
            "cvrmse_percent": 2.0812360472439875,
            "rms_normalized_rmse_percent": 0.6004414135018394,
            "reference_energy": 8.486303725720063,
            "candidate_energy": 8.480106753951986,
            "relative_energy_error_percent": 0.07302321444488426,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 5.476176738739014e-07,
              "p95": 1.3578683137893677e-05,
              "p99": 7.374770939350128e-05,
              "maximum": 0.00024214189033955336
            },
            "worst": {
              "global_sensor_index": 11,
              "local_sensor_index": 11,
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
            "nmbe_percent": 78.65117296914829,
            "cvrmse_percent": 448.5613282214788,
            "rms_normalized_rmse_percent": 30.20634753687306,
            "reference_energy": 2.762939708453928,
            "candidate_energy": 4.936024197583308,
            "relative_energy_error_percent": 78.65117296914828,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00039286998799070716,
              "p95": 0.0005053780041635036,
              "p99": 0.0008719253819435835,
              "maximum": 0.016181334853172302
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032544076442718506,
              "candidate": 0.04872541129589081,
              "position": [
                3.5,
                3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 19.262517786560934,
            "cvrmse_percent": 110.15615293309682,
            "rms_normalized_rmse_percent": 30.20209387093548,
            "reference_energy": 11.24924343417399,
            "candidate_energy": 13.416130951535294,
            "relative_energy_error_percent": 19.262517786560934,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00038990937173366547,
              "p95": 0.0005057388916611671,
              "p99": 0.0008639553561806679,
              "maximum": 0.016181334853172302
            },
            "worst": {
              "global_sensor_index": 12,
              "local_sensor_index": 12,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.032544076442718506,
              "candidate": 0.04872541129589081,
              "position": [
                3.5,
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
      "bias_percent": 0.23930040187474003,
      "rms_normalized_error_percent": 0.32474299999018597,
      "absolute_error": {
        "p95": 0.21805105384444784,
        "p99": 0.3087220050075933,
        "maximum": 0.332418719246931
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 25.168324563064687,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.32474299999018597
    },
    "overcast": {
      "bias_percent": 0.17730215745272862,
      "rms_normalized_error_percent": 0.2499693246716855,
      "absolute_error": {
        "p95": 0.09091606140136715,
        "p99": 0.14455172538757322,
        "maximum": 0.1600179672241211
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 16.276609420776367,
      "reference_fraction_of_uniform": 0.6467100381851196,
      "rms_normalized_to_uniform_percent": 0.17384536497435266
    },
    "horizon": {
      "bias_percent": 1.4373110603698944,
      "rms_normalized_error_percent": 2.8016545547136635,
      "absolute_error": {
        "p95": 0.11808147217683136,
        "p99": 0.17351701566785163,
        "maximum": 0.18923835775522413
      },
      "worst_index": [
        12
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.133517674105409,
      "reference_fraction_of_uniform": 0.08476995235655908,
      "rms_normalized_to_uniform_percent": 0.17721487830218693
    },
    "north": {
      "bias_percent": -46.211266264367275,
      "rms_normalized_error_percent": 105.44358978226283,
      "absolute_error": {
        "p95": 9.551007788104468e-05,
        "p99": 0.00021637277299305416,
        "maximum": 0.00025191347231157124
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 2.9612163416459225e-05,
      "reference_fraction_of_uniform": 1.1765647514039301e-06,
      "rms_normalized_to_uniform_percent": 0.00017590422542274425
    },
    "east": {
      "bias_percent": 0.1596751344980125,
      "rms_normalized_error_percent": 0.2634649700187145,
      "absolute_error": {
        "p95": 0.04388316869735717,
        "p99": 0.05333475351333618,
        "maximum": 0.05609416961669922
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.157871723175049,
      "reference_fraction_of_uniform": 0.20493504405021667,
      "rms_normalized_to_uniform_percent": 0.0599491471599425
    },
    "south": {
      "bias_percent": 0.30065925575729197,
      "rms_normalized_error_percent": 0.4364730972315474,
      "absolute_error": {
        "p95": 0.22021427154540998,
        "p99": 0.28211365699768065,
        "maximum": 0.2967205047607422
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 17.143150329589844,
      "reference_fraction_of_uniform": 0.6811398863792419,
      "rms_normalized_to_uniform_percent": 0.2807532907103137
    },
    "west": {
      "bias_percent": 0.16079968549575083,
      "rms_normalized_error_percent": 0.32520374461189067,
      "absolute_error": {
        "p95": 0.042303544282913205,
        "p99": 0.05282292366027831,
        "maximum": 0.05588388442993164
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 4.993851184844971,
      "reference_fraction_of_uniform": 0.19841809570789337,
      "rms_normalized_to_uniform_percent": 0.07093142354359197
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
        "identifier": "teaching_depth4_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.13290138753244587,
          "cvrmse_percent": 1.1953985289260047,
          "absolute_error_percentiles_lux": {
            "p50": 3.5231475830078125,
            "p90": 33.91096801757813,
            "p95": 52.581372070312426,
            "p99": 108.94583007812497
          },
          "maximum_absolute_error_lux": 503.9833984375,
          "worst": {
            "sensor_index": 8,
            "position": [
              2.5,
              3.5,
              0.75
            ],
            "hour_of_year": 1116.5,
            "foton_lux": 14740.4375,
            "radiance_lux": 14236.4541015625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.12989155251141535,
            "maximum_error_percentage_points": 0.5191780821917718,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.05023202627488743,
            "maximum_error_percentage_points": 0.20117323677294507,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.04656392694063897,
            "maximum_error_percentage_points": 0.19041095890410986,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09071917808219403,
            "maximum_error_percentage_points": 0.32712328767123466,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.08742009132420099,
            "maximum_error_percentage_points": 0.3297260273972604,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 100.0,
          "radiance_percent": 100.0,
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
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004902343750003979,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_depth4_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_depth4_grid",
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
      "study_preparation_seconds": 0.006957457982935011,
      "weather_seconds": 0.10629675001837313,
      "metric_reduction_seconds": 0.04350287502165884,
      "write_seconds": 0.029171583941206336,
      "total_seconds": 0.17913312499877065,
      "cold_end_to_end_seconds": 0.18609058298170567,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.010154166026040912,
      "engine_upload_seconds": 0.00030925,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.024298708303831518,
      "engine_annual_reduction_seconds": 0.00025629159063100815,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.024298708303831518
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006957457982935011,
      "weather_seconds": 0.10574770893435925,
      "metric_reduction_seconds": 0.01171933300793171,
      "write_seconds": 0.027034958940930665,
      "total_seconds": 0.14466850005555898,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.14466850005555898,
      "raw_export_seconds": 0.009276916040107608,
      "engine_upload_seconds": 5.8208e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.00024949992075562477,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.007519040955230594,
      "full": 0.015036916942335665
    }
  },
  "elapsed_seconds": 30.70279449992813,
  "result_class": "passed"
}
```
