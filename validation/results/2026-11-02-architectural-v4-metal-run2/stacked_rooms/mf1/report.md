# Foton report

Status: **passed**

```json
{
  "scene": "stacked_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "stacked_rooms",
    "category": "connections",
    "question": "Does an opaque shared slab isolate two storeys?",
    "interactions": [
      "stacked_zones",
      "opaque_adjacency",
      "room_isolation"
    ],
    "room_count": 2,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 2,
    "apertures": 2,
    "shades": 0,
    "sensors": 72,
    "floor_area": 72.0,
    "aperture_area": 5.999999999999997
  },
  "sky_density": 1,
  "status": "passed",
  "passed": true,
  "model_sha256": "2ee09b87e02506de28a9ff4e6541af9f1849efc815ac6e1bf38b76eca615c3b6",
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
      "scene_fingerprint": 6348620744982744529,
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
      "scene_fingerprint": 6348620744982744529,
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
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": -0.07931914448047922,
        "rms_normalized_error_percent": 1.0753890946716322,
        "absolute_error": {
          "p95": 3.595137968659345e-06,
          "p99": 9.213294833898544e-05,
          "maximum": 0.0003254120238125324
        },
        "worst_index": [
          9,
          72,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": -0.0793895981759524,
        "rms_normalized_error_percent": 1.0753908507263903,
        "absolute_error": {
          "p95": 3.595137968659345e-06,
          "p99": 9.213294833898544e-05,
          "maximum": 0.0003254120238125324
        },
        "worst_index": [
          9,
          72,
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
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": 0.02669685489978009,
        "rms_normalized_error_percent": 1.111361606932977,
        "absolute_error": {
          "p95": 4.529301077127435e-05,
          "p99": 0.00015264004468917847,
          "maximum": 0.0005162004381418228
        },
        "worst_index": [
          1,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": 0.1376837862354315,
        "rms_normalized_error_percent": 1.058042334503945,
        "absolute_error": {
          "p95": 4.058491031173613e-05,
          "p99": 0.00014354498125612736,
          "maximum": 0.00048246048390865326
        },
        "worst_index": [
          8,
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
        "identifier": "stacked_rooms_0_grid",
        "bias_percent": -0.0046304999548813985,
        "rms_normalized_error_percent": 0.9031822755043185,
        "absolute_error": {
          "p95": 3.6282905784901134e-05,
          "p99": 0.0001231962814927101,
          "maximum": 0.0005067829042673111
        },
        "worst_index": [
          26,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "bias_percent": -0.044674536900656855,
        "rms_normalized_error_percent": 0.898186421565967,
        "absolute_error": {
          "p95": 4.012403078377247e-05,
          "p99": 0.00011962559074163437,
          "maximum": 0.00039301812648773193
        },
        "worst_index": [
          8,
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
          "rms_normalized_rmse_percent": 5.0,
          "absolute_energy_bias_percent": 1.0
        },
        "grids": [
          {
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.05493969139243407,
                "cvrmse_percent": 15.100278355608879,
                "rms_normalized_rmse_percent": 3.0831958367412975,
                "reference_energy": 6.01781993086297,
                "candidate_energy": 6.014513759164402,
                "relative_energy_error_percent": 0.05493969139243407,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 6.760603719158087e-05,
                  "p99": 0.0003385784802958369,
                  "maximum": 0.0007175165228545666
                },
                "worst": {
                  "global_sensor_index": 10,
                  "local_sensor_index": 10,
                  "sky_patch_index": 44,
                  "rgb_channel": 0,
                  "reference": 0.00736971665173769,
                  "candidate": 0.006652200128883123
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.6342885166211171,
                "cvrmse_percent": 55.284401294449836,
                "rms_normalized_rmse_percent": 3.0556853831586586,
                "reference_energy": 2.0747108983087728,
                "candidate_energy": 2.087870551289832,
                "relative_energy_error_percent": 0.6342885166211171,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.3422708434518427e-05,
                  "p95": 0.00010664823639672205,
                  "p99": 0.00039389729499816895,
                  "maximum": 0.0008413353934884071
                },
                "worst": {
                  "global_sensor_index": 25,
                  "local_sensor_index": 25,
                  "sky_patch_index": 18,
                  "rgb_channel": 0,
                  "reference": 0.0010285824537277222,
                  "candidate": 0.00018724706023931503
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.05972108932546196,
                "cvrmse_percent": 12.297522904458528,
                "rms_normalized_rmse_percent": 2.5152743775382014,
                "reference_energy": 6.015388640422316,
                "candidate_energy": 6.0117961847990955,
                "relative_energy_error_percent": 0.05972108932546196,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 7.025876220723147e-05,
                  "p99": 0.0002463452983647585,
                  "maximum": 0.0006726091960445046
                },
                "worst": {
                  "global_sensor_index": 52,
                  "local_sensor_index": 16,
                  "sky_patch_index": 95,
                  "rgb_channel": 0,
                  "reference": 0.0072207103949040174,
                  "candidate": 0.006548101198859513
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.22780734755390575,
                "cvrmse_percent": 51.11048699405661,
                "rms_normalized_rmse_percent": 2.834800487969951,
                "reference_energy": 2.080828691667314,
                "candidate_energy": 2.085568972316942,
                "relative_energy_error_percent": 0.22780734755390578,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 1.2465375675674295e-05,
                  "p95": 0.00011242453474551404,
                  "p99": 0.0003622361982706934,
                  "maximum": 0.00098249816801399
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 9,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": -0.0004664636217057705,
                  "candidate": 0.0005160345463082194
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 145.73041594121605,
            "full": 393.99283309467137
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 143.03216710686684,
            "full": 405.1219579996541
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 145.61724988743663,
            "full": 392.51562498975545
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 136.95820805151016,
            "full": 393.1347910547629
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 138.70479096658528,
            "full": 398.3869159128517
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 164.92841602303088,
            "full": 412.1608749264851
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 153.4674580907449,
            "full": 405.8132920181379
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 137.6694169593975,
            "full": 400.0821659574285
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.1868157789986342,
                "cvrmse_percent": 8.01610411660727,
                "rms_normalized_rmse_percent": 1.6412279389036395,
                "reference_energy": 6.022771697382268,
                "candidate_energy": 6.011520209518494,
                "relative_energy_error_percent": 0.18681577899863416,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.550013800326266e-05,
                  "p99": 0.0001801024191081524,
                  "maximum": 0.00037205638363957405
                },
                "worst": {
                  "global_sensor_index": 14,
                  "local_sensor_index": 14,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.007483103545382619,
                  "candidate": 0.007855159929022193
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.3070254585397602,
                "cvrmse_percent": 20.874827300049333,
                "rms_normalized_rmse_percent": 1.8015373287682148,
                "reference_energy": 3.8108285234574133,
                "candidate_energy": 3.8225287372057224,
                "relative_energy_error_percent": 0.3070254585397602,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.1531599969648596e-07,
                  "p90": 3.0095754482317716e-05,
                  "p95": 7.98136926277947e-05,
                  "p99": 0.0002685160143300891,
                  "maximum": 0.0005540899001061916
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.0003636060282588005,
                  "candidate": -0.00019048387184739113
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.06393918963870632,
                "cvrmse_percent": 7.553190753785184,
                "rms_normalized_rmse_percent": 1.5452796253036167,
                "reference_energy": 6.018275311907928,
                "candidate_energy": 6.014427275443268,
                "relative_energy_error_percent": 0.06393918963870632,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.5373756438493726e-05,
                  "p99": 0.00016266084276139736,
                  "maximum": 0.000349988229572773
                },
                "worst": {
                  "global_sensor_index": 58,
                  "local_sensor_index": 22,
                  "sky_patch_index": 46,
                  "rgb_channel": 0,
                  "reference": 0.007459001149982214,
                  "candidate": 0.007808989379554987
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.17900929985015165,
                "cvrmse_percent": 19.2893664373007,
                "rms_normalized_rmse_percent": 1.6668182286152684,
                "reference_energy": 3.8141134084887263,
                "candidate_energy": 3.8209410261967527,
                "relative_energy_error_percent": 0.17900929985015165,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.5941242043359125e-07,
                  "p90": 2.8375477995723486e-05,
                  "p95": 7.770207739667939e-05,
                  "p99": 0.0002512929495424032,
                  "maximum": 0.000524464063346386
                },
                "worst": {
                  "global_sensor_index": 38,
                  "local_sensor_index": 2,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.021538804285228252,
                  "candidate": 0.021014340221881866
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 202.9589160811156,
            "full": 4898.660792037845
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 218.2144159451127,
            "full": 4899.4205829221755
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.52666696999222,
            "full": 4871.065167011693
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 204.5149999903515,
            "full": 4833.268375019543
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.016615833481704877,
                "cvrmse_percent": 9.428194484918853,
                "rms_normalized_rmse_percent": 1.9276825949135064,
                "reference_energy": 6.01648610812299,
                "candidate_energy": 6.0154864188098145,
                "relative_energy_error_percent": 0.016615833481704874,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.522866802290076e-05,
                  "p99": 0.00020730611868202686,
                  "maximum": 0.0004012240096926689
                },
                "worst": {
                  "global_sensor_index": 16,
                  "local_sensor_index": 16,
                  "sky_patch_index": 43,
                  "rgb_channel": 0,
                  "reference": 0.006950872018933296,
                  "candidate": 0.007352096028625965
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": -0.289079111919649,
                "cvrmse_percent": 23.3497832653659,
                "rms_normalized_rmse_percent": 2.02114577949442,
                "reference_energy": 3.8259937340014503,
                "candidate_energy": 3.8149335852930975,
                "relative_energy_error_percent": 0.2890791119196491,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.2237289165616403e-07,
                  "p90": 2.9237900889711455e-05,
                  "p95": 8.75585479661822e-05,
                  "p99": 0.00028775952523574233,
                  "maximum": 0.0007884446531534195
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.0320479441434145,
                  "candidate": 0.03125949949026108
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.08967550643987993,
                "cvrmse_percent": 8.481388969753553,
                "rms_normalized_rmse_percent": 1.7350913606858653,
                "reference_energy": 6.019515315994795,
                "candidate_energy": 6.0141172851499505,
                "relative_energy_error_percent": 0.08967550643987991,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.384287167340515e-05,
                  "p99": 0.00017521437257528305,
                  "maximum": 0.0004547596909105778
                },
                "worst": {
                  "global_sensor_index": 52,
                  "local_sensor_index": 16,
                  "sky_patch_index": 72,
                  "rgb_channel": 0,
                  "reference": 0.013398485258221626,
                  "candidate": 0.013853244949132204
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.5253372423766877,
                "cvrmse_percent": 22.840524513267468,
                "rms_normalized_rmse_percent": 1.9743582996700024,
                "reference_energy": 3.8205664303602376,
                "candidate_energy": 3.8406372886886615,
                "relative_energy_error_percent": 0.5253372423766877,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 2.318800085276962e-07,
                  "p90": 2.985595347126946e-05,
                  "p95": 8.346398535650198e-05,
                  "p99": 0.0002894848585128784,
                  "maximum": 0.0006178845651447773
                },
                "worst": {
                  "global_sensor_index": 52,
                  "local_sensor_index": 16,
                  "sky_patch_index": 72,
                  "rgb_channel": 0,
                  "reference": 0.0006173397414386272,
                  "candidate": -5.448237061500549e-07
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 203.38962494861335,
            "full": 5219.046333921142
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 197.22416705917567,
            "full": 5140.011167037301
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 199.76212503388524,
            "full": 5092.758540995419
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 198.73758300673217,
            "full": 5185.410209000111
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
            "identifier": "stacked_rooms_0_grid",
            "start_sensor_index": 0,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": -0.045607619080756875,
                "cvrmse_percent": 4.165342827399052,
                "rms_normalized_rmse_percent": 0.8515409830052699,
                "reference_energy": 6.014289598315372,
                "candidate_energy": 6.011546624024959,
                "relative_energy_error_percent": 0.04560761908075688,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.358733909204598e-05,
                  "p99": 8.211692329496145e-05,
                  "maximum": 0.00017825979739427567
                },
                "worst": {
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "sky_patch_index": 75,
                  "rgb_channel": 0,
                  "reference": 0.013206135015934706,
                  "candidate": 0.013384394813328981
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.04305425754303373,
                "cvrmse_percent": 13.366152070439659,
                "rms_normalized_rmse_percent": 1.1576102011602574,
                "reference_energy": 3.822253491140124,
                "candidate_energy": 3.823899134002147,
                "relative_energy_error_percent": 0.04305425754303373,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.679067409554591e-07,
                  "p90": 2.0155646780040115e-05,
                  "p95": 4.457043833099298e-05,
                  "p99": 0.00016800552839413285,
                  "maximum": 0.0006983205676078796
                },
                "worst": {
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.031515900045633316,
                  "candidate": 0.032214220613241196
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "start_sensor_index": 36,
            "sensor_count": 36,
            "stages": {
              "direct": {
                "nmbe_percent": 0.005326768681560522,
                "cvrmse_percent": 4.284381975817884,
                "rms_normalized_rmse_percent": 0.8759470989549842,
                "reference_energy": 6.016028909979923,
                "candidate_energy": 6.016349369923773,
                "relative_energy_error_percent": 0.005326768681560522,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.3462291574105612e-05,
                  "p99": 9.156810119748116e-05,
                  "maximum": 0.00019465479999780655
                },
                "worst": {
                  "global_sensor_index": 62,
                  "local_sensor_index": 26,
                  "sky_patch_index": 48,
                  "rgb_channel": 0,
                  "reference": 0.005852562608197331,
                  "candidate": 0.006047217408195138
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.12379268044012806,
                "cvrmse_percent": 12.489466100059254,
                "rms_normalized_rmse_percent": 1.0812382375923348,
                "reference_energy": 3.8244625333129143,
                "candidate_energy": 3.829196937995331,
                "relative_energy_error_percent": 0.12379268044012806,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 1.569286780522816e-07,
                  "p90": 2.0251944079063833e-05,
                  "p95": 4.447300088941118e-05,
                  "p99": 0.0001523345708847046,
                  "maximum": 0.0004796348512172699
                },
                "worst": {
                  "global_sensor_index": 66,
                  "local_sensor_index": 30,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.014975714962929487,
                  "candidate": 0.015455349814146757
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 321.94725004956126,
            "full": 9095.72212502826
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 314.1615829663351,
            "full": 9110.933165997267
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 328.1059580622241,
            "full": 9080.133375013247
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 322.89533293806016,
            "full": 9073.4997499967
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 2924.1122499806806,
      "worker_pool_size": 12,
      "invocation_count": 5
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/stacked_rooms/mf1/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 10989.94825000409,
      "worker_pool_size": 12,
      "invocation_count": 5
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      72,
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.045817622317891354,
            "cvrmse_percent": 3.4361133159179285,
            "rms_normalized_rmse_percent": 0.7026164804842399,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04581762231789136,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.1046477535300585,
            "cvrmse_percent": 24.28439764316917,
            "rms_normalized_rmse_percent": 2.101034070092254,
            "reference_energy": 3.8188866975688605,
            "candidate_energy": 3.776701451454308,
            "relative_energy_error_percent": 1.1046477535300585,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.643318843340239e-07,
              "p90": 3.8427475374192e-05,
              "p95": 5.719949185731818e-05,
              "p99": 0.00012397393584251404,
              "maximum": 0.0013891607522964478
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031865060329437256,
              "candidate": 0.030475899577140808,
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
            "nmbe_percent": -0.45691507962496564,
            "cvrmse_percent": 9.355044344309613,
            "rms_normalized_rmse_percent": 2.084649811365776,
            "reference_energy": 9.835994436839474,
            "candidate_energy": 9.791052295026482,
            "relative_energy_error_percent": 0.45691507962496564,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.643318843340239e-07,
              "p90": 3.7873694964218885e-05,
              "p95": 5.547136242967097e-05,
              "p99": 0.00011288956739008427,
              "maximum": 0.0013891607522964478
            },
            "worst": {
              "global_sensor_index": 21,
              "local_sensor_index": 21,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.031865060329437256,
              "candidate": 0.030475899577140808,
              "position": [
                3.5,
                2.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04574714495092785,
            "cvrmse_percent": 3.436127666028291,
            "rms_normalized_rmse_percent": 0.7026190577945717,
            "reference_energy": 6.017103496630625,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04574714495092785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.4322187528013656e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.8698339309687089,
            "cvrmse_percent": 23.35413513621766,
            "rms_normalized_rmse_percent": 2.022265810387821,
            "reference_energy": 3.8259154046204635,
            "candidate_energy": 3.792636294260916,
            "relative_energy_error_percent": 0.8698339309687088,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 5.97875271068915e-07,
              "p90": 3.613793523982167e-05,
              "p95": 5.513464348041452e-05,
              "p99": 0.00015529897063970566,
              "maximum": 0.0013143345713615417
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029842594638466835,
              "candidate": 0.028528260067105293,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.3660641494188204,
            "cvrmse_percent": 9.008401825535902,
            "rms_normalized_rmse_percent": 2.0068511263824047,
            "reference_energy": 9.843018901251089,
            "candidate_energy": 9.80698713783309,
            "relative_energy_error_percent": 0.3660641494188204,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 5.88902310028061e-07,
              "p90": 3.6206518416292965e-05,
              "p95": 5.5831475037848557e-05,
              "p99": 0.00013078702613711357,
              "maximum": 0.0013143345713615417
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.029842594638466835,
              "candidate": 0.028528260067105293,
              "position": [
                1.5,
                1.5,
                3.75
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
        "identifier": "stacked_rooms_0_grid",
        "full_identifier": "stacked_rooms_0_grid",
        "start_sensor_index": 0,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.045817622317891354,
            "cvrmse_percent": 3.4361133159179285,
            "rms_normalized_rmse_percent": 0.7026164804842399,
            "reference_energy": 6.017107739270614,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04581762231789136,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.2354885004460016e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 10,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.5416534810038,
            "cvrmse_percent": 436.05487296633737,
            "rms_normalized_rmse_percent": 24.1796526457903,
            "reference_energy": 2.0803498145121253,
            "candidate_energy": 3.776701451454308,
            "relative_energy_error_percent": 81.5416534810038,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00021965010091662407,
              "p95": 0.000288426445331424,
              "p99": 0.0004957974888384342,
              "maximum": 0.007958583533763885
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011405566707253456,
              "candidate": 0.01936415024101734,
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
            "nmbe_percent": 20.915141944184413,
            "cvrmse_percent": 112.00678294134103,
            "rms_normalized_rmse_percent": 24.17494801181495,
            "reference_energy": 8.09745755378274,
            "candidate_energy": 9.791052295026482,
            "relative_energy_error_percent": 20.915141944184413,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00021941956219961867,
              "p95": 0.0002895621153584214,
              "p99": 0.0004906555695924908,
              "maximum": 0.007958583533763885
            },
            "worst": {
              "global_sensor_index": 35,
              "local_sensor_index": 35,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011405566707253456,
              "candidate": 0.01936415024101734,
              "position": [
                5.5,
                0.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "full_identifier": "stacked_rooms_1_grid",
        "start_sensor_index": 36,
        "sensor_count": 36,
        "stages": {
          "direct": {
            "nmbe_percent": -0.04574714495092785,
            "cvrmse_percent": 3.436127666028291,
            "rms_normalized_rmse_percent": 0.7026190577945717,
            "reference_energy": 6.017103496630625,
            "candidate_energy": 6.014350843572174,
            "relative_energy_error_percent": 0.04574714495092785,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 2.4322187528013656e-06,
              "p99": 5.3141440730541945e-05,
              "maximum": 0.00031554256565868855
            },
            "worst": {
              "global_sensor_index": 46,
              "local_sensor_index": 10,
              "sky_patch_index": 96,
              "rgb_channel": 0,
              "reference": 0.002480260794982314,
              "candidate": 0.0027958033606410027,
              "position": [
                1.5,
                1.5,
                3.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 82.36565830934825,
            "cvrmse_percent": 439.8104004514979,
            "rms_normalized_rmse_percent": 24.386560147468277,
            "reference_energy": 2.0796877709439343,
            "candidate_energy": 3.792636294260916,
            "relative_energy_error_percent": 82.36565830934823,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022233973140828311,
              "p95": 0.0002895898753195069,
              "p99": 0.0004948696587234735,
              "maximum": 0.008471760898828506
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01577152870595455,
              "candidate": 0.024243289604783058,
              "position": [
                5.5,
                1.5,
                3.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 21.12189648641924,
            "cvrmse_percent": 112.94594868019158,
            "rms_normalized_rmse_percent": 24.38206658422859,
            "reference_energy": 8.09679126757456,
            "candidate_energy": 9.80698713783309,
            "relative_energy_error_percent": 21.12189648641924,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.00022157438479553093,
              "p95": 0.0002886219925130716,
              "p99": 0.0004673016956076026,
              "maximum": 0.008471760898828506
            },
            "worst": {
              "global_sensor_index": 70,
              "local_sensor_index": 34,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.01577152870595455,
              "candidate": 0.024243289604783058,
              "position": [
                5.5,
                1.5,
                3.75
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
      "bias_percent": 0.1331403752523499,
      "rms_normalized_error_percent": 0.23988362945504574,
      "absolute_error": {
        "p95": 0.110121491364975,
        "p99": 0.13201877085756156,
        "maximum": 0.1413560798753717
      },
      "worst_index": [
        54
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 12.02959438889406,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.23988362945504574
    },
    "overcast": {
      "bias_percent": 0.08709732596714699,
      "rms_normalized_error_percent": 0.2093653890850381,
      "absolute_error": {
        "p95": 0.06658279895782473,
        "p99": 0.0870065784454347,
        "maximum": 0.10262680053710938
      },
      "worst_index": [
        59
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 7.680564880371094,
      "reference_fraction_of_uniform": 0.6384724974632263,
      "rms_normalized_to_uniform_percent": 0.14769095365070462
    },
    "horizon": {
      "bias_percent": 0.98906571043314,
      "rms_normalized_error_percent": 2.215367563931169,
      "absolute_error": {
        "p95": 0.061392599304858,
        "p99": 0.07909143347730939,
        "maximum": 0.0919666028110182
      },
      "worst_index": [
        60
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1215015944905378,
      "reference_fraction_of_uniform": 0.0932285460535501,
      "rms_normalized_to_uniform_percent": 0.12562751724017196
    },
    "north": {
      "bias_percent": -27.39011094133922,
      "rms_normalized_error_percent": 151.718407935497,
      "absolute_error": {
        "p95": 5.024346523896384e-05,
        "p99": 8.335163338415458e-05,
        "maximum": 0.0001026774352794746
      },
      "worst_index": [
        16
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.1753180842788424e-05,
      "reference_fraction_of_uniform": 9.770221822691383e-07,
      "rms_normalized_to_uniform_percent": 0.0001156847221160171
    },
    "east": {
      "bias_percent": 0.09162304133469683,
      "rms_normalized_error_percent": 0.3347995886342443,
      "absolute_error": {
        "p95": 0.027798652648925785,
        "p99": 0.03914870262146004,
        "maximum": 0.047606468200683594
      },
      "worst_index": [
        40
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.451352834701538,
      "reference_fraction_of_uniform": 0.20377685129642487,
      "rms_normalized_to_uniform_percent": 0.07159671018279713
    },
    "south": {
      "bias_percent": 0.1709907685141457,
      "rms_normalized_error_percent": 0.2834026305835252,
      "absolute_error": {
        "p95": 0.08417801856994632,
        "p99": 0.10754350423812867,
        "maximum": 0.10871744155883789
      },
      "worst_index": [
        54
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 8.306821823120117,
      "reference_fraction_of_uniform": 0.6905321478843689,
      "rms_normalized_to_uniform_percent": 0.18468580932184112
    },
    "west": {
      "bias_percent": 0.05897122257771052,
      "rms_normalized_error_percent": 0.36714760499939386,
      "absolute_error": {
        "p95": 0.035208404064178474,
        "p99": 0.04290492773056042,
        "maximum": 0.055912017822265625
      },
      "worst_index": [
        65
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 2.3682031631469727,
      "reference_fraction_of_uniform": 0.1968647539615631,
      "rms_normalized_to_uniform_percent": 0.07518310867604805
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
        "identifier": "stacked_rooms_0_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": -0.05077265008879458,
          "cvrmse_percent": 1.5779419493068692,
          "absolute_error_percentiles_lux": {
            "p50": 2.43438720703125,
            "p90": 24.16212158203125,
            "p95": 35.6513671875,
            "p99": 63.70950988769529
          },
          "maximum_absolute_error_lux": 414.32666015625,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              0.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5148.72216796875,
            "radiance_lux": 5563.048828125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.39201674277016746,
            "maximum_error_percentage_points": 2.030547945205477,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.1368597315166495,
            "maximum_error_percentage_points": 0.7579720012293052,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.09696727549467231,
            "maximum_error_percentage_points": 0.3563013698630151,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.09760273972602758,
            "maximum_error_percentage_points": 0.3006849315068507,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.023245814307458024,
            "maximum_error_percentage_points": 0.13630136986301267,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 58.333333333333336,
          "radiance_percent": 55.55555555555556,
          "difference_percentage_points": 2.7777777777777786,
          "tolerance_percentage_points": 2.7777777777777777,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "stacked_rooms_1_grid",
        "sensor_count": 36,
        "illuminance": {
          "nmbe_percent": 0.034009718378959684,
          "cvrmse_percent": 1.6176970148196297,
          "absolute_error_percentiles_lux": {
            "p50": 2.4668807983398438,
            "p90": 24.05496215820314,
            "p95": 36.39737548828121,
            "p99": 69.2427032470703
          },
          "maximum_absolute_error_lux": 310.77490234375,
          "worst": {
            "sensor_index": 28,
            "position": [
              4.5,
              1.5,
              3.75
            ],
            "hour_of_year": 5246.5,
            "foton_lux": 5181.8408203125,
            "radiance_lux": 5492.61572265625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.347914764079147,
            "maximum_error_percentage_points": 1.3386301369863034,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.14455040948077683,
            "maximum_error_percentage_points": 0.8085911455217598,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.1292161339421615,
            "maximum_error_percentage_points": 0.6579452054794501,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.12927701674276904,
            "maximum_error_percentage_points": 0.6621917808219138,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.021864535768645305,
            "maximum_error_percentage_points": 0.1115068493150666,
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
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004865689212323332,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004681078767120539,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
            "maximum_error_percentage_points": 0.004794520547944714,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "stacked_rooms_0_grid",
            "maximum_error_percentage_points": 0.004931506849315426,
            "passed": true
          },
          {
            "identifier": "stacked_rooms_1_grid",
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
      "study_preparation_seconds": 0.009171499987132847,
      "weather_seconds": 0.10606783302500844,
      "metric_reduction_seconds": 0.06645366596058011,
      "write_seconds": 0.04894270794466138,
      "total_seconds": 0.22163141600321978,
      "cold_end_to_end_seconds": 0.23080291599035263,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.023983250022865832,
      "engine_upload_seconds": 0.000267708,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.04788129182998091,
      "engine_annual_reduction_seconds": 0.0005930834449827671,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.04788129182998091
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.009171499987132847,
      "weather_seconds": 0.10217754205223173,
      "metric_reduction_seconds": 0.013293207972310483,
      "write_seconds": 0.05395720899105072,
      "total_seconds": 0.16958675009664148,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.16958675009664148,
      "raw_export_seconds": 0.032688917010091245,
      "engine_upload_seconds": 5.2875e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.001096041640266776,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.008052708930335939,
      "full": 0.0420645420672372
    }
  },
  "elapsed_seconds": 100.07032437506132,
  "result_class": "passed"
}
```
