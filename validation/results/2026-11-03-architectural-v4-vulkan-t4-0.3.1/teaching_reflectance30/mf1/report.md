# Foton report

Status: **passed**

```json
{
  "scene": "teaching_reflectance30",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "teaching_reflectance30",
    "category": "teaching",
    "question": "How much does 0.3 surface reflectance cost at the back of the room?",
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
  "model_sha256": "d02f9dfd056053f9a476e70587e8b35b65cd68e110abb61e74192ecb63f12d9b",
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 8544998466427496008,
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
      "solver_version": "0.3.1",
      "scene_fingerprint": 8544998466427496008,
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
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 65536,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/content/bundle/foton-references-corpus4-2026-11-03",
    "model_sha256": "f9bd3bc0fecc15cf6df5af270c37e1839aba46454d06d67cbcf4cc801f29c55c",
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
        "identifier": "teaching_reflectance30_grid",
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
          "maximum": 0.0003680046647787094,
          "p95": 6.145127117633814e-05,
          "p99": 0.00015048589557409286
        },
        "bias_percent": -0.06154341989054886,
        "identifier": "teaching_reflectance30_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.0723160594423093,
        "worst_index": [
          21,
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
          "maximum": 0.00043931975960731506,
          "p95": 4.761552554555232e-05,
          "p99": 0.00012397486716508865
        },
        "bias_percent": -0.007546624643115694,
        "identifier": "teaching_reflectance30_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.899776732898179,
        "worst_index": [
          33,
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
            "identifier": "teaching_reflectance30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.000546684954315424,
                  "p50": 0.0,
                  "p90": 8.200295269489288e-07,
                  "p95": 0.0001001377240754658,
                  "p99": 0.00026880245422944427
                },
                "candidate_energy": 8.954063132905503,
                "cvrmse_percent": 9.05519097661692,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.1207847803716912,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.943261034706666,
                "relative_energy_error_percent": 0.1207847803716912,
                "rms_normalized_rmse_percent": 2.2363522281347605,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.01379472529515624,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.013248040340840816,
                  "rgb_channel": 0,
                  "sky_patch_index": 72
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0010726714972406626,
                  "p50": 0.0,
                  "p90": 3.8168858736753464e-05,
                  "p95": 0.00018931797530967695,
                  "p99": 0.0004806893412023783
                },
                "candidate_energy": 1.868750811097211,
                "cvrmse_percent": 78.75843115157377,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.13571457707394913,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 1.86621808112114,
                "relative_energy_error_percent": 0.13571457707394913,
                "rms_normalized_rmse_percent": 3.5169981538631947,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0002267553936690092,
                  "global_sensor_index": 7,
                  "local_sensor_index": 7,
                  "reference": -0.0012994268909096718,
                  "rgb_channel": 0,
                  "sky_patch_index": 44
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.9072080552578,
            "full": 250.07549999281764
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.14683294203132,
            "full": 231.77245794795454
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 116.5277500404045,
            "full": 256.0475829523057
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 132.47929199133068,
            "full": 242.5746249500662
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
            "identifier": "teaching_reflectance30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00037626607809215784,
                  "p50": 0.0,
                  "p90": 1.93051528185606e-06,
                  "p95": 8.958166581578529e-05,
                  "p99": 0.000210681464523077
                },
                "candidate_energy": 8.953011164655436,
                "cvrmse_percent": 7.3732901869310865,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.08850832928545152,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.94509401139294,
                "relative_energy_error_percent": 0.08850832928545153,
                "rms_normalized_rmse_percent": 1.819271952917471,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0017383400117978454,
                  "global_sensor_index": 17,
                  "local_sensor_index": 17,
                  "reference": 0.002114606089890003,
                  "rgb_channel": 0,
                  "sky_patch_index": 16
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0005679549649357796,
                  "p50": 1.0336221656359612e-07,
                  "p90": 2.4979533918667585e-05,
                  "p95": 0.00011666734935715788,
                  "p99": 0.0002898401580750942
                },
                "candidate_energy": 2.5410950595886312,
                "cvrmse_percent": 34.42936308061947,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.08643234158121554,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.5432932875303216,
                "relative_energy_error_percent": 0.08643234158121554,
                "rms_normalized_rmse_percent": 1.999517246912521,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 8.234987035393715e-05,
                  "global_sensor_index": 34,
                  "local_sensor_index": 34,
                  "reference": 0.0006503048352897167,
                  "rgb_channel": 0,
                  "sky_patch_index": 76
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 162.25904203020036,
            "full": 1432.8427499858662
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 156.69987502042204,
            "full": 1433.2548329839483
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 151.00095805246383,
            "full": 1433.0791250104085
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 166.4992910809815,
            "full": 1474.6431249659508
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
            "identifier": "teaching_reflectance30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003335664514452219,
                  "p50": 0.0,
                  "p90": 1.2852251529693604e-06,
                  "p95": 7.004280923865732e-05,
                  "p99": 0.00018630200065672398
                },
                "candidate_energy": 8.952700107718556,
                "cvrmse_percent": 6.382667284321035,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.02745264253872552,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.950243029493322,
                "relative_energy_error_percent": 0.027452642538725522,
                "rms_normalized_rmse_percent": 1.5754861202188015,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.007243665400892496,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": 0.006910098949447274,
                  "rgb_channel": 0,
                  "sky_patch_index": 43
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006291447207331657,
                  "p50": 1.166873726532458e-07,
                  "p90": 2.4055945686995983e-05,
                  "p95": 0.00011986313620582218,
                  "p99": 0.0002822054666467011
                },
                "candidate_energy": 2.5328429963468224,
                "cvrmse_percent": 35.32456194466671,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.011047260432316443,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.532563217492573,
                "relative_energy_error_percent": 0.011047260432316445,
                "rms_normalized_rmse_percent": 2.044351495787276,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.00023464998230338097,
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "reference": -0.0003944947384297848,
                  "rgb_channel": 0,
                  "sky_patch_index": 71
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.2522079590708,
            "full": 1454.7567499103025
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 176.5810839133337,
            "full": 1432.7907500555739
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 169.0093750366941,
            "full": 1479.8237920040265
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 167.45195793919265,
            "full": 1474.4764160132036
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
            "identifier": "teaching_reflectance30_grid",
            "sensor_count": 36,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0002207868965342641,
                  "p50": 0.0,
                  "p90": 7.440103217959404e-07,
                  "p95": 4.306964110583066e-05,
                  "p99": 0.00010325387120246887
                },
                "candidate_energy": 8.947597222112563,
                "cvrmse_percent": 3.414321910629467,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.0144562587697977,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 8.946303921267372,
                "relative_energy_error_percent": 0.0144562587697977,
                "rms_normalized_rmse_percent": 0.8424396199454475,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003734202473424375,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.003513415576890111,
                  "rgb_channel": 0,
                  "sky_patch_index": 47
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00037499936297535896,
                  "p50": 7.926607281660836e-08,
                  "p90": 1.5209625416900963e-05,
                  "p95": 6.617355393245814e-05,
                  "p99": 0.00016986578702926636
                },
                "candidate_energy": 2.5381768502087816,
                "cvrmse_percent": 20.51799916902834,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.14357092162124446,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.534537990656755,
                "relative_energy_error_percent": 0.14357092162124446,
                "rms_normalized_rmse_percent": 1.1881124935886251,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.015436755027621984,
                  "global_sensor_index": 19,
                  "local_sensor_index": 19,
                  "reference": 0.015811754390597343,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 219.31379195302725,
            "full": 2473.2070839963853
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 224.04195903800428,
            "full": 2428.9429580094293
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 216.2738749757409,
            "full": 2428.7753750104457
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 220.91637505218387,
            "full": 2477.022874983959
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
    "/content/suite-vulkan-0.3.1/teaching_reflectance30/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 873.8914999412373,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/teaching_reflectance30/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 2857.124542002566,
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
        "identifier": "teaching_reflectance30_grid",
        "full_identifier": "teaching_reflectance30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.057234207925190565,
            "cvrmse_percent": 2.4774773209699803,
            "rms_normalized_rmse_percent": 0.6117134404603434,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272118650493,
            "relative_energy_error_percent": 0.057234207925190565,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.249168654903633e-06,
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
            "nmbe_percent": -1.059087198171075,
            "cvrmse_percent": 28.481358692447653,
            "rms_normalized_rmse_percent": 1.6460076411887192,
            "reference_energy": 2.5299114801947393,
            "candidate_energy": 2.5031175115829365,
            "relative_energy_error_percent": 1.0590871981710748,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.236638962926918e-07,
              "p90": 2.087168104480952e-05,
              "p95": 4.123430990148333e-05,
              "p99": 0.00011335499584674835,
              "maximum": 0.001030903309583664
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023957662284374237,
              "candidate": 0.022926758974790573,
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
            "nmbe_percent": -0.27795452479843646,
            "cvrmse_percent": 6.246695404372624,
            "rms_normalized_rmse_percent": 1.638638525786411,
            "reference_energy": 11.48330800442828,
            "candidate_energy": 11.451389630233429,
            "relative_energy_error_percent": 0.2779545247984442,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.2219830952963093e-07,
              "p90": 2.0672334358096123e-05,
              "p95": 4.076755176356513e-05,
              "p99": 0.00010849535465240479,
              "maximum": 0.001030903309583664
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.023957662284374237,
              "candidate": 0.022926758974790573,
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
        "identifier": "teaching_reflectance30_grid",
        "full_identifier": "teaching_reflectance30_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.057234207925190565,
            "cvrmse_percent": 2.4774773209699803,
            "rms_normalized_rmse_percent": 0.6117134404603434,
            "reference_energy": 8.95339652423354,
            "candidate_energy": 8.948272118650493,
            "relative_energy_error_percent": 0.057234207925190565,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 1.2898817658424377e-07,
              "p95": 6.249168654903633e-06,
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
            "nmbe_percent": 34.37753082661999,
            "cvrmse_percent": 169.19537037013578,
            "rms_normalized_rmse_percent": 7.538325757148896,
            "reference_energy": 1.8627500417555467,
            "candidate_energy": 2.5031175115829365,
            "relative_energy_error_percent": 34.37753082661999,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.656837210059166e-05,
              "p95": 0.00014736254670424375,
              "p99": 0.0003284076228737831,
              "maximum": 0.0030508171766996384
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00964738242328167,
              "candidate": 0.012698199599981308,
              "position": [
                3.5,
                5.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 5.873099632745714,
            "cvrmse_percent": 29.110950693225895,
            "rms_normalized_rmse_percent": 7.531141299935225,
            "reference_energy": 10.816146565989087,
            "candidate_energy": 11.451389630233429,
            "relative_energy_error_percent": 5.8730996327457055,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 9.635197011448327e-05,
              "p95": 0.0001425825299520511,
              "p99": 0.0003329074243083596,
              "maximum": 0.0030508171766996384
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.00964738242328167,
              "candidate": 0.012698199599981308,
              "position": [
                3.5,
                5.5,
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
      "bias_percent": 0.0796574006477688,
      "rms_normalized_error_percent": 0.1503424612662778,
      "absolute_error": {
        "p95": 0.07752840762180735,
        "p99": 0.08011794937805229,
        "maximum": 0.08131912247171602
      },
      "worst_index": [
        6
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 15.903667003145065,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.1503424612662778
    },
    "overcast": {
      "bias_percent": 0.04998408683227496,
      "rms_normalized_error_percent": 0.12711234155748272,
      "absolute_error": {
        "p95": 0.0463109016418457,
        "p99": 0.05562763214111328,
        "maximum": 0.056980133056640625
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.264345169067383,
      "reference_fraction_of_uniform": 0.6454074382781982,
      "rms_normalized_to_uniform_percent": 0.08938563134653552
    },
    "horizon": {
      "bias_percent": 1.0276272515673017,
      "rms_normalized_error_percent": 1.7458283910372976,
      "absolute_error": {
        "p95": 0.05352649473058663,
        "p99": 0.06940158323232871,
        "maximum": 0.07360671474270641
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.2801855514001519,
      "reference_fraction_of_uniform": 0.0804962497735262,
      "rms_normalized_to_uniform_percent": 0.0890432489358133
    },
    "north": {
      "bias_percent": -76.37303958832364,
      "rms_normalized_error_percent": 101.7056258778247,
      "absolute_error": {
        "p95": 9.005227821035078e-05,
        "p99": 0.00023235941553139127,
        "maximum": 0.00023602238798048347
      },
      "worst_index": [
        8
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.703273483144585e-05,
      "reference_fraction_of_uniform": 1.070994130714098e-06,
      "rms_normalized_to_uniform_percent": 0.00020686241858499247
    },
    "east": {
      "bias_percent": -0.0076589615073389345,
      "rms_normalized_error_percent": 0.1689468549793616,
      "absolute_error": {
        "p95": 0.01943764090538025,
        "p99": 0.023804336786270135,
        "maximum": 0.02574300765991211
      },
      "worst_index": [
        3
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.192232370376587,
      "reference_fraction_of_uniform": 0.20072303712368011,
      "rms_normalized_to_uniform_percent": 0.03832395292348247
    },
    "south": {
      "bias_percent": 0.10594907314634411,
      "rms_normalized_error_percent": 0.19203945181771065,
      "absolute_error": {
        "p95": 0.07197636365890503,
        "p99": 0.07448688745498658,
        "maximum": 0.07482743263244629
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.958486557006836,
      "reference_fraction_of_uniform": 0.6890540719032288,
      "rms_normalized_to_uniform_percent": 0.12238364136892708
    },
    "west": {
      "bias_percent": 0.03449686478611584,
      "rms_normalized_error_percent": 0.22446328165460822,
      "absolute_error": {
        "p95": 0.027209758758544922,
        "p99": 0.032945394515991204,
        "maximum": 0.03383159637451172
      },
      "worst_index": [
        34
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.093945264816284,
      "reference_fraction_of_uniform": 0.19454288482666016,
      "rms_normalized_to_uniform_percent": 0.048774467605813526
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
        "identifier": "teaching_reflectance30_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.028636439759317883,
          "cvrmse_percent": 0.958473938282643,
          "absolute_error_percentiles_lux": {
            "p50": 1.5726852416992188,
            "p90": 13.430987548828126,
            "p95": 22.235922241210933,
            "p99": 55.16772338867166
          },
          "maximum_absolute_error_lux": 336.106201171875,
          "worst": {
            "sensor_index": 34,
            "position": [
              5.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 3797.473388671875,
            "radiance_lux": 4133.57958984375
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.2813318112633188,
            "maximum_error_percentage_points": 2.1943835616438356,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.14098391695851595,
            "maximum_error_percentage_points": 0.7853761353993605,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.12801369863013706,
            "maximum_error_percentage_points": 0.6339726027397248,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.1278424657534266,
            "maximum_error_percentage_points": 0.6339726027397319,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.03058599695586007,
            "maximum_error_percentage_points": 0.1934246575342442,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 55.55555555555556,
          "radiance_percent": 55.55555555555556,
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
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.004885488013698591,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "teaching_reflectance30_grid",
            "maximum_error_percentage_points": 0.004520547945205511,
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
      "study_preparation_seconds": 0.3587605729990173,
      "weather_seconds": 0.24633639999956358,
      "metric_reduction_seconds": 0.15202686400152743,
      "write_seconds": 0.048384139001427684,
      "total_seconds": 0.4471513450043858,
      "cold_end_to_end_seconds": 0.8059119180034031,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.03565479799726745,
      "engine_upload_seconds": 0.013514922,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.011943991,
      "engine_annual_reduction_seconds": 0.006899753,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.011943991
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.3587605729990173,
      "weather_seconds": 0.2323575959962909,
      "metric_reduction_seconds": 0.14469151500088628,
      "write_seconds": 0.020387757998832967,
      "total_seconds": 0.3977714740030933,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.3977714740030933,
      "raw_export_seconds": 0.008487070001137909,
      "engine_upload_seconds": 0.013655269,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 5.1e-08,
      "engine_annual_reduction_seconds": 0.007015432,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.013944530001026578,
      "full": 0.020956706001015846
    }
  },
  "elapsed_seconds": 2.595573903003242,
  "result_class": "passed"
}
```
