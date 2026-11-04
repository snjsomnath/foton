# Foton report

Status: **passed**

```json
{
  "scene": "trapezoid_plan",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "trapezoid_plan",
    "category": "form",
    "question": "How do splayed walls change illumination and reflections?",
    "interactions": [
      "angled_walls",
      "nonorthogonal_plan"
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
    "floor_area": 56.0,
    "aperture_area": 2.999999999999999
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "a10a6fa8703513aa10ab094cdb41edad952de58758daaf485d8d53acd518cca9",
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 4702131747089679607,
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
      "solver_version": "0.3.2",
      "scene_fingerprint": 4702131747089679607,
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
  "sky_sources": {
    "candidate": {
      "sky_source": "foton",
      "sky_version": "foton-sky-r1 (foton-daylight 0.3.2)",
      "weather_id": "82c544d76aea9710a570440071d4833104fdc7da7504bac286ac2afe42bdd614"
    },
    "reference": {
      "sky_source": "gendaymtx",
      "sky_version": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)",
      "gendaymtx": "/usr/local/radiance/bin/gendaymtx",
      "weather_id": "a39080f6e203418927f730315e529393ad080464468f645476c383a744bbb720"
    },
    "sun_up_hours_equal": true,
    "compared_hours": 4405,
    "max_relative_difference": 0.0,
    "mean_relative_difference": 0.0
  },
  "settings": {
    "direct_samples": 256,
    "maximum_samples": 262144,
    "maximum_bounces": 8
  },
  "direct_io": "binary",
  "oracle_stable": true,
  "reference_source": {
    "bundle": "/private/tmp/claude-501/-Users-ssanjay-GitHub/12f3d0b2-7d1e-44d9-9264-d1e29a27929b/scratchpad/refx/foton-references-corpus4-2026-11-03",
    "model_sha256": "f3443938a9d3da3c14d3728719ff84e383f4f808542b864281dd393cbfcf455c",
    "model_sha256_matches": false,
    "sensor_grid_sha256": "2ac629109977a30bc8fd8526a56056c521e654eb0c97d50fb92079cd8ec06be6",
    "sensor_grid_sha256_matches": true,
    "sensor_grid_max_difference": 0.0,
    "geometry_matches": true,
    "one_bounce_replicates": 4
  },
  "direct_stability": {
    "grids": [
      {
        "absolute_error": {
          "maximum": 0.00014028436271473765,
          "p95": 4.307366907596588e-09,
          "p99": 5.990557838231325e-06
        },
        "bias_percent": -0.02205826350872095,
        "identifier": "trapezoid_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 0.7692756919556606,
        "worst_index": [
          23,
          543,
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
          "maximum": 0.0005748756229877472,
          "p95": 1.4675286365672946e-05,
          "p99": 9.647072874940932e-05
        },
        "bias_percent": 0.08621287947758366,
        "identifier": "trapezoid_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 2.0633889829971612,
        "worst_index": [
          28,
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
          "maximum": 0.00048436783254146576,
          "p95": 1.2277352652745321e-05,
          "p99": 7.748871576040983e-05
        },
        "bias_percent": -0.03386574494558745,
        "identifier": "trapezoid_plan_grid",
        "passed": true,
        "rms_normalized_error_percent": 1.6398363446989999,
        "worst_index": [
          43,
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0005108050536364317,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 0.0,
                  "p99": 0.00015769805759191513
                },
                "candidate_energy": 6.173454506912094,
                "cvrmse_percent": 38.28971992869483,
                "energy_difference_negligible": false,
                "nmbe_percent": 0.10610888626684113,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.166910866474609,
                "relative_energy_error_percent": 0.10610888626684113,
                "rms_normalized_rmse_percent": 6.531739506313141,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.00471619563177228,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.004205390578135848,
                  "rgb_channel": 0,
                  "sky_patch_index": 519
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00096893310546875,
                  "p50": 0.0,
                  "p90": 1.3920316632720642e-07,
                  "p95": 2.2906531285116216e-05,
                  "p99": 0.0002659205929376185
                },
                "candidate_energy": 2.0594578618543835,
                "cvrmse_percent": 189.08553013251895,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.035817442372482286,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 2.0601957712875247,
                "relative_energy_error_percent": 0.035817442372482286,
                "rms_normalized_rmse_percent": 6.315349466406952,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": -0.0005725194932892919,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.00039641361217945814,
                  "rgb_channel": 0,
                  "sky_patch_index": 260
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 126.641791081056,
            "full": 275.2421669429168
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.15429202094674,
            "full": 275.9117499226704
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 121.06670904904604,
            "full": 276.8012919696048
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 125.95879100263119,
            "full": 278.8314170902595
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003220511134713888,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.0653820936568081e-08,
                  "p99": 0.00013130251318216324
                },
                "candidate_energy": 6.171551917425859,
                "cvrmse_percent": 29.54003433538215,
                "energy_difference_negligible": true,
                "nmbe_percent": -0.010160897555556297,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.172179066217723,
                "relative_energy_error_percent": 0.010160897555556297,
                "rms_normalized_rmse_percent": 5.037669185385879,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0035812905989587307,
                  "global_sensor_index": 28,
                  "local_sensor_index": 28,
                  "reference": 0.003259239485487342,
                  "rgb_channel": 0,
                  "sky_patch_index": 266
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006476342678070068,
                  "p50": 0.0,
                  "p90": 1.0596759238978848e-05,
                  "p95": 2.251609112136066e-05,
                  "p99": 0.0001679975539445877
                },
                "candidate_energy": 3.7459999630738423,
                "cvrmse_percent": 71.43964500512617,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": 0.0715033942142129,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.743323359815161,
                "relative_energy_error_percent": 0.0715033942142129,
                "rms_normalized_rmse_percent": 3.535648101756712,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.028586735017597675,
                  "global_sensor_index": 21,
                  "local_sensor_index": 21,
                  "reference": 0.02793910074979067,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 158.2139590755105,
            "full": 2992.9292920278385
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 165.20379099529237,
            "full": 3049.2557079996914
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 159.19525001663715,
            "full": 2971.059540985152
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 153.82112504448742,
            "full": 2945.311874966137
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.0003454923862591386,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.396438165102154e-08,
                  "p99": 0.000117497518658638
                },
                "candidate_energy": 6.169806748588599,
                "cvrmse_percent": 28.28354655163509,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.03912875242589374,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.167393524445288,
                "relative_energy_error_percent": 0.03912875242589375,
                "rms_normalized_rmse_percent": 4.823961510609627,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.003907718462869525,
                  "global_sensor_index": 23,
                  "local_sensor_index": 23,
                  "reference": 0.0035622260766103864,
                  "rgb_channel": 0,
                  "sky_patch_index": 357
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.0006438447162508965,
                  "p50": 3.552713678800501e-15,
                  "p90": 1.0409209153294796e-05,
                  "p95": 2.2119644199847244e-05,
                  "p99": 0.00018086674390360713
                },
                "candidate_energy": 3.75457964371833,
                "cvrmse_percent": 71.12270455378402,
                "energy_difference_negligible": true,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.10093269144169241,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7583730708131213,
                "relative_energy_error_percent": 0.10093269144169244,
                "rms_normalized_rmse_percent": 3.524021493364705,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.031536584720015526,
                  "global_sensor_index": 22,
                  "local_sensor_index": 22,
                  "reference": 0.03089274000376463,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 161.63845802657306,
            "full": 3233.6491249734536
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 157.6975000789389,
            "full": 3149.1520409472287
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.299499980174,
            "full": 3257.6118749566376
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 155.56550002656877,
            "full": 3262.987458962016
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
          "rms_normalized_rmse_percent": 10.0
        },
        "grids": [
          {
            "identifier": "trapezoid_plan_grid",
            "sensor_count": 48,
            "stages": {
              "direct": {
                "absolute_error": {
                  "maximum": 0.00019251700723543763,
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1583324521780014e-08,
                  "p99": 6.295798812061548e-05
                },
                "candidate_energy": 6.170376106189451,
                "cvrmse_percent": 14.837278065809125,
                "energy_difference_negligible": true,
                "nmbe_percent": 0.01744433733101481,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 6.169299912701717,
                "relative_energy_error_percent": 0.01744433733101481,
                "rms_normalized_rmse_percent": 2.5314759244997465,
                "rms_normalized_to": "stage",
                "worst": {
                  "candidate": 0.0016835815040394664,
                  "global_sensor_index": 43,
                  "local_sensor_index": 43,
                  "reference": 0.0014910644968040287,
                  "rgb_channel": 0,
                  "sky_patch_index": 159
                }
              },
              "indirect": {
                "absolute_error": {
                  "maximum": 0.00037255510687828064,
                  "p50": 8.822622632465027e-09,
                  "p90": 7.340062438743189e-06,
                  "p95": 1.5067606000229716e-05,
                  "p99": 9.824300650507212e-05
                },
                "candidate_energy": 3.7491674031768767,
                "cvrmse_percent": 40.66895881246404,
                "energy_difference_negligible": false,
                "negligible_relative_to_direct": false,
                "nmbe_percent": -0.14434826010384075,
                "passed": true,
                "physically_near_zero": false,
                "reference_energy": 3.7545870843071576,
                "relative_energy_error_percent": 0.14434826010384075,
                "rms_normalized_rmse_percent": 2.0139252200677484,
                "rms_normalized_to": "full",
                "worst": {
                  "candidate": 0.011036585085093975,
                  "global_sensor_index": 38,
                  "local_sensor_index": 38,
                  "reference": 0.010664029978215694,
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 232.4140410637483,
            "full": 5725.302582955919
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 253.98429099004716,
            "full": 5700.16708294861
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 242.83875001128763,
            "full": 5685.1178330834955
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct"
            ]
          ],
          "timings_ms": {
            "direct": 229.83995801769197,
            "full": 5687.463290989399
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
    "/Users/ssanjay/GitHub/foton-release-0.3.2/validation/results/2026-11-04-architectural-v4-metal-0.3.2-release/trapezoid_plan/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 4768.630790989846,
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
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-03-architectural-v4-metal-0.3.0/trapezoid_plan/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "elapsed_ms": 19480.999874998815,
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
      48,
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
        "identifier": "trapezoid_plan_grid",
        "full_identifier": "trapezoid_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02829377655892921,
            "cvrmse_percent": 2.515426050218017,
            "rms_normalized_rmse_percent": 0.42938349663125924,
            "reference_energy": 6.169195072863658,
            "candidate_energy": 6.167449574594258,
            "relative_energy_error_percent": 0.028293776558929215,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.862645149230957e-09,
              "p99": 4.94916457682848e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -1.4262016363339753,
            "cvrmse_percent": 57.52810945023872,
            "rms_normalized_rmse_percent": 2.847094732222705,
            "reference_energy": 3.752520217567975,
            "candidate_energy": 3.699001712821257,
            "relative_energy_error_percent": 1.4262016363339753,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 8.116563549265265e-06,
              "p95": 1.322513708146289e-05,
              "p99": 4.059448838233948e-05,
              "maximum": 0.0012810919433832169
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.028573282063007355,
              "candidate": 0.027292190119624138,
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
            "nmbe_percent": -0.5570004923383971,
            "cvrmse_percent": 21.733727158111076,
            "rms_normalized_rmse_percent": 2.8439355248102616,
            "reference_energy": 9.921715290431633,
            "candidate_energy": 9.866451287415515,
            "relative_energy_error_percent": 0.5570004923383971,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 2.4999996739438757e-08,
              "p90": 8.082326530711725e-06,
              "p95": 1.3161276001483202e-05,
              "p99": 3.9740465581417084e-05,
              "maximum": 0.0012810919433832169
            },
            "worst": {
              "global_sensor_index": 28,
              "local_sensor_index": 28,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.028573282063007355,
              "candidate": 0.027292190119624138,
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
      48,
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
        "identifier": "trapezoid_plan_grid",
        "full_identifier": "trapezoid_plan_grid",
        "start_sensor_index": 0,
        "sensor_count": 48,
        "stages": {
          "direct": {
            "nmbe_percent": -0.02829377655892921,
            "cvrmse_percent": 2.515426050218017,
            "rms_normalized_rmse_percent": 0.42938349663125924,
            "reference_energy": 6.169195072863658,
            "candidate_energy": 6.167449574594258,
            "relative_energy_error_percent": 0.028293776558929215,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 1.862645149230957e-09,
              "p99": 4.94916457682848e-06,
              "maximum": 5.9494748711586e-05
            },
            "worst": {
              "global_sensor_index": 15,
              "local_sensor_index": 15,
              "sky_patch_index": 307,
              "rgb_channel": 0,
              "reference": 0.0027457945980131626,
              "candidate": 0.0028052893467247486,
              "position": [
                1.5,
                1.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 79.49222573647283,
            "cvrmse_percent": 767.006552019801,
            "rms_normalized_rmse_percent": 25.571567459664795,
            "reference_energy": 2.0608144434355964,
            "candidate_energy": 3.699001712821257,
            "relative_energy_error_percent": 79.49222573647285,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.397999873617664e-05,
              "p95": 6.274993938859552e-05,
              "p99": 0.0001437345054000616,
              "maximum": 0.005770397372543812
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011129791848361492,
              "candidate": 0.016900189220905304,
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
            "nmbe_percent": 19.883838139862934,
            "cvrmse_percent": 192.04840226191536,
            "rms_normalized_rmse_percent": 25.569981996608927,
            "reference_energy": 8.230009516299255,
            "candidate_energy": 9.866451287415515,
            "relative_energy_error_percent": 19.883838139862934,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 4.402999911690131e-05,
              "p95": 6.26499968348071e-05,
              "p99": 0.000143763842061162,
              "maximum": 0.005770397372543812
            },
            "worst": {
              "global_sensor_index": 9,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.011129791848361492,
              "candidate": 0.016900189220905304,
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
      "bias_percent": 0.16719107092932028,
      "rms_normalized_error_percent": 0.14153567942077083,
      "absolute_error": {
        "p95": 0.04847664637253697,
        "p99": 0.05690029639208623,
        "maximum": 0.06344356100370385
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 9.090894458400173,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.14153567942077083
    },
    "overcast": {
      "bias_percent": 0.12388624063938729,
      "rms_normalized_error_percent": 0.10951627305690266,
      "absolute_error": {
        "p95": 0.029453110694885244,
        "p99": 0.034518127441406254,
        "maximum": 0.036533355712890625
      },
      "worst_index": [
        23
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 5.810382843017578,
      "reference_fraction_of_uniform": 0.6391431093215942,
      "rms_normalized_to_uniform_percent": 0.07814431932304541
    },
    "horizon": {
      "bias_percent": 0.9706033194496752,
      "rms_normalized_error_percent": 1.8943569025127143,
      "absolute_error": {
        "p95": 0.044583375399237034,
        "p99": 0.06273281837148341,
        "maximum": 0.07320714585955668
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.1067632470728757,
      "reference_fraction_of_uniform": 0.12174415313448103,
      "rms_normalized_to_uniform_percent": 0.12132722873151015
    },
    "north": {
      "bias_percent": -90.70916310263098,
      "rms_normalized_error_percent": 100.02449071291062,
      "absolute_error": {
        "p95": 9.487780480412764e-05,
        "p99": 0.00019348298637737572,
        "maximum": 0.00019789290672633797
      },
      "worst_index": [
        28
      ],
      "passed": true,
      "physically_near_zero": true,
      "negligible": false,
      "reference_mean": 1.7440866940887645e-05,
      "reference_fraction_of_uniform": 1.9184983557352098e-06,
      "rms_normalized_to_uniform_percent": 0.00025159791592578205
    },
    "east": {
      "bias_percent": 0.09947746262844144,
      "rms_normalized_error_percent": 0.1851767369469002,
      "absolute_error": {
        "p95": 0.015992033481597896,
        "p99": 0.01800037741661072,
        "maximum": 0.018716812133789062
      },
      "worst_index": [
        14
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.6960357427597046,
      "reference_fraction_of_uniform": 0.18656422197818756,
      "rms_normalized_to_uniform_percent": 0.036925065028428496
    },
    "south": {
      "bias_percent": 0.22529018330287356,
      "rms_normalized_error_percent": 0.19350490349054789,
      "absolute_error": {
        "p95": 0.04326297044754028,
        "p99": 0.06251397132873536,
        "maximum": 0.0663149356842041
      },
      "worst_index": [
        24
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 6.3617424964904785,
      "reference_fraction_of_uniform": 0.6997928023338318,
      "rms_normalized_to_uniform_percent": 0.126238148476631
    },
    "west": {
      "bias_percent": 0.08584298461189227,
      "rms_normalized_error_percent": 0.1724829235862675,
      "absolute_error": {
        "p95": 0.012653017044067382,
        "p99": 0.015635239630937582,
        "maximum": 0.01742386817932129
      },
      "worst_index": [
        47
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 1.720170021057129,
      "reference_fraction_of_uniform": 0.18921899795532227,
      "rms_normalized_to_uniform_percent": 0.034679638729459464
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
        "identifier": "trapezoid_plan_grid",
        "sensor_count": 48,
        "illuminance": {
          "nmbe_percent": 0.04154152356913943,
          "cvrmse_percent": 1.9049211765385832,
          "absolute_error_percentiles_lux": {
            "p50": 1.6033744812011719,
            "p90": 18.444873046875003,
            "p95": 28.956010437011706,
            "p99": 65.12407836914038
          },
          "maximum_absolute_error_lux": 374.62890625,
          "worst": {
            "sensor_index": 22,
            "position": [
              2.5,
              1.5,
              0.75
            ],
            "hour_of_year": 2868.5,
            "foton_lux": 12518.7314453125,
            "radiance_lux": 12893.3603515625
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.26389840182648483,
            "maximum_error_percentage_points": 0.9839726027397262,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.18789730909478575,
            "maximum_error_percentage_points": 0.7210450065571052,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.14648401826484073,
            "maximum_error_percentage_points": 0.7939726027397285,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.14527111872146112,
            "maximum_error_percentage_points": 0.7687671232876667,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.015585045662100441,
            "maximum_error_percentage_points": 0.07821917808219181,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 29.166666666666668,
          "radiance_percent": 29.166666666666668,
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
      "maximum_error_percentage_points": 0.004951840753427916,
      "metrics": {
        "da": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004951840753427916,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.00479452054794649,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "trapezoid_plan_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "trapezoid_plan_grid",
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
      "study_preparation_seconds": 0.006351624964736402,
      "weather_seconds": 0.08465408405754715,
      "metric_reduction_seconds": 0.1314488749485463,
      "write_seconds": 0.01449450000654906,
      "total_seconds": 0.23073358298279345,
      "cold_end_to_end_seconds": 0.23708520794752985,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.0021990829845890403,
      "engine_upload_seconds": 0.000817041,
      "engine_acceleration_structure_seconds": 0.0029987919999999997,
      "engine_tracing_seconds": 0.06919079180806875,
      "engine_annual_reduction_seconds": 0.0029351665871217847,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.06919079180806875
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.006351624964736402,
      "weather_seconds": 0.07854641694575548,
      "metric_reduction_seconds": 0.04951816704124212,
      "write_seconds": 0.019124416983686388,
      "total_seconds": 0.1473254170268774,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.1473254170268774,
      "raw_export_seconds": 0.002492500003427267,
      "engine_upload_seconds": 5.3791e-05,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.0021828750614076853,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015551958931609988,
      "full": 0.08361879200674593
    }
  },
  "elapsed_seconds": 1.5450624170480296,
  "result_class": "passed"
}
```
