# Foton report

Status: **passed**

```json
{
  "scene": "courtyard_rooms",
  "scene_spec": {
    "suite_version": 4,
    "identifier": "courtyard_rooms",
    "category": "connections",
    "question": "Do four inward-facing rooms shade one another beneath a pergola?",
    "interactions": [
      "multiroom_context",
      "courtyard",
      "combined_shading"
    ],
    "room_count": 4,
    "include_glazing": true,
    "footprint_family": null,
    "window_profile": null
  },
  "model_summary": {
    "rooms": 4,
    "apertures": 4,
    "shades": 4,
    "sensors": 112,
    "floor_area": 112.0,
    "aperture_area": 17.999999999999996
  },
  "sky_density": 2,
  "status": "passed",
  "passed": true,
  "model_sha256": "2ef815d189cb6f9f1f804d12e4734e55b6b81cd9f61669b712af2479848522a5",
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
      "scene_fingerprint": 16353448696249269853,
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
      "scene_fingerprint": 16353448696249269853,
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
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": -0.06178634245362834,
        "rms_normalized_error_percent": 2.0054789116125984,
        "absolute_error": {
          "p95": 2.225817434009452e-06,
          "p99": 5.3780851885676384e-05,
          "maximum": 0.000219903071410954
        },
        "worst_index": [
          20,
          257,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": -0.038772710182519515,
        "rms_normalized_error_percent": 1.7126260035610261,
        "absolute_error": {
          "p95": 1.8526833628129107e-06,
          "p99": 4.403468687087163e-05,
          "maximum": 0.00020035728812217712
        },
        "worst_index": [
          20,
          281,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": -0.029120901909352463,
        "rms_normalized_error_percent": 1.7911551555114564,
        "absolute_error": {
          "p95": 6.941612809896469e-06,
          "p99": 5.37758693099015e-05,
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
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": 0.1452844111884245,
        "rms_normalized_error_percent": 1.8407748689157513,
        "absolute_error": {
          "p95": 6.831385235273046e-06,
          "p99": 5.762645887443718e-05,
          "maximum": 0.0001625253353267908
        },
        "worst_index": [
          14,
          285,
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
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": 0.007862334454470573,
        "rms_normalized_error_percent": 1.401085973381876,
        "absolute_error": {
          "p95": 2.5961445339816755e-05,
          "p99": 9.820339269935941e-05,
          "maximum": 0.000588495284318924
        },
        "worst_index": [
          27,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": 0.0670630581547009,
        "rms_normalized_error_percent": 1.3716803687924526,
        "absolute_error": {
          "p95": 2.6473541947779536e-05,
          "p99": 0.00010051046498119713,
          "maximum": 0.0004937350749969482
        },
        "worst_index": [
          19,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": -0.024335405729148777,
        "rms_normalized_error_percent": 1.362755207546666,
        "absolute_error": {
          "p95": 3.4804121241904795e-05,
          "p99": 0.00011812031734734731,
          "maximum": 0.0004713311791419983
        },
        "worst_index": [
          17,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": 0.11856475865476322,
        "rms_normalized_error_percent": 1.332864632483592,
        "absolute_error": {
          "p95": 3.6750396247953176e-05,
          "p99": 0.00011483829002827382,
          "maximum": 0.00038463249802589417
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
  "sample_stability": {
    "passed": true,
    "grids": [
      {
        "identifier": "courtyard_rooms_west_grid",
        "bias_percent": 0.0292149418056492,
        "rms_normalized_error_percent": 1.2941578507664295,
        "absolute_error": {
          "p95": 2.2469612486019962e-05,
          "p99": 8.486549806548199e-05,
          "maximum": 0.0006946660578250885
        },
        "worst_index": [
          10,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "bias_percent": 0.003529758657057663,
        "rms_normalized_error_percent": 1.1076362135244544,
        "absolute_error": {
          "p95": 2.28138655529619e-05,
          "p99": 7.900893921032515e-05,
          "maximum": 0.00042069703340530396
        },
        "worst_index": [
          3,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "bias_percent": 0.11077531472984246,
        "rms_normalized_error_percent": 1.1653052329568743,
        "absolute_error": {
          "p95": 2.9836082831025124e-05,
          "p99": 9.585695806890652e-05,
          "maximum": 0.0006968341767787933
        },
        "worst_index": [
          11,
          0,
          0
        ],
        "passed": true
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "bias_percent": -0.012660492292030014,
        "rms_normalized_error_percent": 1.181958293446041,
        "absolute_error": {
          "p95": 2.919438702519983e-05,
          "p99": 9.470543591305539e-05,
          "maximum": 0.0006474032998085022
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.0860134793569348,
                "cvrmse_percent": 38.15006544157883,
                "rms_normalized_rmse_percent": 7.59977969120373,
                "reference_energy": 5.717079075204907,
                "candidate_energy": 5.721996533835078,
                "relative_energy_error_percent": 0.0860134793569348,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.0039601299212306e-05,
                  "p99": 0.00021834503160789512,
                  "maximum": 0.0006472350214608014
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 199,
                  "rgb_channel": 0,
                  "reference": 0.0018509160145185888,
                  "candidate": 0.00249815103597939
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.1940232890868823,
                "cvrmse_percent": 138.0678499285213,
                "rms_normalized_rmse_percent": 5.252708886954121,
                "reference_energy": 2.3937951256079515,
                "candidate_energy": 2.3984396456446575,
                "relative_energy_error_percent": 0.19402328908688227,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.3642805899726227e-05,
                  "p95": 6.440892775572085e-05,
                  "p99": 0.0003219171037198975,
                  "maximum": 0.0008734388975426555
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 192,
                  "rgb_channel": 0,
                  "reference": 0.0004146014107391238,
                  "candidate": -0.00045883748680353165
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.18578052693130315,
                "cvrmse_percent": 38.28347524613603,
                "rms_normalized_rmse_percent": 7.63638287814547,
                "reference_energy": 5.732644007473709,
                "candidate_energy": 5.721993871229529,
                "relative_energy_error_percent": 0.18578052693130315,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.423522703086967e-05,
                  "p99": 0.0002220913680503131,
                  "maximum": 0.000651646318146959
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 12,
                  "sky_patch_index": 169,
                  "rgb_channel": 0,
                  "reference": 0.0013030729605816305,
                  "candidate": 0.0006514266424346715
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.016327670863255914,
                "cvrmse_percent": 137.96897468761335,
                "rms_normalized_rmse_percent": 5.24700231720466,
                "reference_energy": 2.4062321375738236,
                "candidate_energy": 2.4058392559101947,
                "relative_energy_error_percent": 0.016327670863255914,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 2.36457162827719e-05,
                  "p95": 6.49805044474759e-05,
                  "p99": 0.0003216760326176863,
                  "maximum": 0.0011024810373783112
                },
                "worst": {
                  "global_sensor_index": 35,
                  "local_sensor_index": 3,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04456407018005848,
                  "candidate": 0.04346158914268017
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.050583205274476406,
                "cvrmse_percent": 35.51959795222305,
                "rms_normalized_rmse_percent": 7.95909973772466,
                "reference_energy": 5.354343971345955,
                "candidate_energy": 5.351635572543827,
                "relative_energy_error_percent": 0.0505832052744764,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.7288223868235946e-05,
                  "p99": 0.00023559632463729935,
                  "maximum": 0.0007297050324268639
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "sky_patch_index": 262,
                  "rgb_channel": 0,
                  "reference": 0.002046798530500382,
                  "candidate": 0.002776503562927246
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.17204162762265085,
                "cvrmse_percent": 124.8265373611852,
                "rms_normalized_rmse_percent": 5.21058783422658,
                "reference_energy": 2.2723952463191246,
                "candidate_energy": 2.2763047120869118,
                "relative_energy_error_percent": 0.17204162762265085,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.138704389333725e-05,
                  "p95": 8.838542271405458e-05,
                  "p99": 0.00036975330731365603,
                  "maximum": 0.0010038124746643007
                },
                "worst": {
                  "global_sensor_index": 74,
                  "local_sensor_index": 10,
                  "sky_patch_index": 262,
                  "rgb_channel": 0,
                  "reference": 0.0005929964245297015,
                  "candidate": -0.0004108160501345992
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05515407102102327,
                "cvrmse_percent": 35.12638883281796,
                "rms_normalized_rmse_percent": 7.843782783426596,
                "reference_energy": 5.359224234802667,
                "candidate_energy": 5.362180065143306,
                "relative_energy_error_percent": 0.05515407102102327,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.759192233905196e-05,
                  "p99": 0.00023468443687306697,
                  "maximum": 0.0006509859813377261
                },
                "worst": {
                  "global_sensor_index": 102,
                  "local_sensor_index": 14,
                  "sky_patch_index": 239,
                  "rgb_channel": 0,
                  "reference": 0.002232661470770836,
                  "candidate": 0.0015816754894331098
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.2815057285893318,
                "cvrmse_percent": 138.74909754599202,
                "rms_normalized_rmse_percent": 5.743274333823563,
                "reference_energy": 2.196189111450721,
                "candidate_energy": 2.190006713291332,
                "relative_energy_error_percent": 0.2815057285893318,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 4.3294359784340486e-05,
                  "p95": 9.405792866346019e-05,
                  "p99": 0.0003647265344625328,
                  "maximum": 0.0024915989488363266
                },
                "worst": {
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.048373524099588394,
                  "candidate": 0.04588192515075207
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 281.5416670637205,
            "full": 861.5819170372561
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 247.0625420100987,
            "full": 803.4727919148281
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 259.5564170042053,
            "full": 775.8906669914722
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 255.3427079692483,
            "full": 801.3167500030249
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.05944736398065292,
                "cvrmse_percent": 22.28942360552209,
                "rms_normalized_rmse_percent": 4.447818424170159,
                "reference_energy": 5.72267249484878,
                "candidate_energy": 5.726074472796213,
                "relative_energy_error_percent": 0.05944736398065292,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1647937410307284e-05,
                  "p99": 0.00013129315222613512,
                  "maximum": 0.00038428051630035043
                },
                "worst": {
                  "global_sensor_index": 29,
                  "local_sensor_index": 29,
                  "sky_patch_index": 246,
                  "rgb_channel": 0,
                  "reference": 0.0016275939997285604,
                  "candidate": 0.002011874516028911
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.38767443104920024,
                "cvrmse_percent": 46.99789268757727,
                "rms_normalized_rmse_percent": 2.462046022322174,
                "reference_energy": 4.393710253166635,
                "candidate_energy": 4.376676961940721,
                "relative_energy_error_percent": 0.38767443104920024,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.4517725843462586e-06,
                  "p90": 2.310833842500415e-05,
                  "p95": 4.2615437996573565e-05,
                  "p99": 0.00018529190507251747,
                  "maximum": 0.0008773449808359146
                },
                "worst": {
                  "global_sensor_index": 18,
                  "local_sensor_index": 18,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.041947634890675545,
                  "candidate": 0.04107028990983963
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.1282042188996655,
                "cvrmse_percent": 23.269207758389236,
                "rms_normalized_rmse_percent": 4.639892718539255,
                "reference_energy": 5.7237077259201214,
                "candidate_energy": 5.731045760702237,
                "relative_energy_error_percent": 0.1282042188996655,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.167394059142673e-05,
                  "p99": 0.000134514614474028,
                  "maximum": 0.00038684962783008814
                },
                "worst": {
                  "global_sensor_index": 43,
                  "local_sensor_index": 11,
                  "sky_patch_index": 377,
                  "rgb_channel": 0,
                  "reference": 0.0029111490584909916,
                  "candidate": 0.0025242994306609035
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.1554194912461118,
                "cvrmse_percent": 49.713276189308495,
                "rms_normalized_rmse_percent": 2.607373899059524,
                "reference_energy": 4.391549206292289,
                "candidate_energy": 4.384723882858047,
                "relative_energy_error_percent": 0.1554194912461118,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.55267894494682e-06,
                  "p90": 2.3117196178645827e-05,
                  "p95": 4.213441595197757e-05,
                  "p99": 0.0002047651744214812,
                  "maximum": 0.0007239561527967453
                },
                "worst": {
                  "global_sensor_index": 52,
                  "local_sensor_index": 20,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.043736040592193604,
                  "candidate": 0.04301208443939686
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.020401546066509273,
                "cvrmse_percent": 21.771505002274974,
                "rms_normalized_rmse_percent": 4.881067655657,
                "reference_energy": 5.356374337255936,
                "candidate_energy": 5.357467120433846,
                "relative_energy_error_percent": 0.020401546066509273,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.785250009968877e-05,
                  "p99": 0.0001535567862447347,
                  "maximum": 0.00041871750727295876
                },
                "worst": {
                  "global_sensor_index": 82,
                  "local_sensor_index": 18,
                  "sky_patch_index": 153,
                  "rgb_channel": 0,
                  "reference": 0.0015835869708098471,
                  "candidate": 0.0011648694635368884
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.16785503493932682,
                "cvrmse_percent": 45.7349996321714,
                "rms_normalized_rmse_percent": 2.5142090382817086,
                "reference_energy": 4.120130272278548,
                "candidate_energy": 4.127046118386627,
                "relative_energy_error_percent": 0.16785503493932682,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.37192113117635e-06,
                  "p90": 2.8713026267723762e-05,
                  "p95": 5.68395626032725e-05,
                  "p99": 0.00022156301420181917,
                  "maximum": 0.0009069554507732391
                },
                "worst": {
                  "global_sensor_index": 75,
                  "local_sensor_index": 11,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05797402933239937,
                  "candidate": 0.05888098478317261
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.19998280984988265,
                "cvrmse_percent": 20.853790624643853,
                "rms_normalized_rmse_percent": 4.66018435276076,
                "reference_energy": 5.3600420105430615,
                "candidate_energy": 5.349322847921243,
                "relative_energy_error_percent": 0.19998280984988265,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.953473060391843e-05,
                  "p99": 0.0001455751771572973,
                  "maximum": 0.0004162514815106988
                },
                "worst": {
                  "global_sensor_index": 98,
                  "local_sensor_index": 10,
                  "sky_patch_index": 183,
                  "rgb_channel": 0,
                  "reference": 0.002127068000845611,
                  "candidate": 0.0017108165193349123
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.49465503531428556,
                "cvrmse_percent": 45.10753980109505,
                "rms_normalized_rmse_percent": 2.4905219018147466,
                "reference_energy": 4.058874709716694,
                "candidate_energy": 4.0789521378454054,
                "relative_energy_error_percent": 0.49465503531428556,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.213808738664284e-06,
                  "p90": 2.9754770366707817e-05,
                  "p95": 6.316190410871059e-05,
                  "p99": 0.0002264407376060237,
                  "maximum": 0.0006235779728740454
                },
                "worst": {
                  "global_sensor_index": 93,
                  "local_sensor_index": 5,
                  "sky_patch_index": 183,
                  "rgb_channel": 0,
                  "reference": -0.00025015592109411955,
                  "candidate": 0.0003734220517799258
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 348.83304208051413,
            "full": 8648.636333062313
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 312.3311660019681,
            "full": 9761.139792040922
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 441.05562497861683,
            "full": 11304.159207968041
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 434.5438330201432,
            "full": 8814.34616597835
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.09112610590464626,
                "cvrmse_percent": 22.202953708760162,
                "rms_normalized_rmse_percent": 4.4312668934480985,
                "reference_energy": 5.723482125351197,
                "candidate_energy": 5.728697711734178,
                "relative_energy_error_percent": 0.09112610590464626,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.1478372218552824e-05,
                  "p99": 0.00012475812691263452,
                  "maximum": 0.00039464642759412527
                },
                "worst": {
                  "global_sensor_index": 11,
                  "local_sensor_index": 11,
                  "sky_patch_index": 197,
                  "rgb_channel": 0,
                  "reference": 0.0024133684346452355,
                  "candidate": 0.0020187220070511103
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.07907854339612821,
                "cvrmse_percent": 48.58337495004828,
                "rms_normalized_rmse_percent": 2.550740332655016,
                "reference_energy": 4.386006218428395,
                "candidate_energy": 4.382537828597599,
                "relative_energy_error_percent": 0.07907854339612821,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.527279319432864e-06,
                  "p90": 2.3143358930610702e-05,
                  "p95": 4.344506487541332e-05,
                  "p99": 0.00019630368158686837,
                  "maximum": 0.0011060163378715515
                },
                "worst": {
                  "global_sensor_index": 27,
                  "local_sensor_index": 27,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05179421976208687,
                  "candidate": 0.05290023609995842
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0181394599327831,
                "cvrmse_percent": 22.879744298094327,
                "rms_normalized_rmse_percent": 4.564751826214023,
                "reference_energy": 5.728405250755522,
                "candidate_energy": 5.727366148980273,
                "relative_energy_error_percent": 0.0181394599327831,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.140619908459484e-05,
                  "p99": 0.0001273060910170896,
                  "maximum": 0.00042562803719192743
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 12,
                  "sky_patch_index": 322,
                  "rgb_channel": 0,
                  "reference": 0.0039013801142573357,
                  "candidate": 0.0034757520770654082
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.0174682260509613,
                "cvrmse_percent": 48.09163172504709,
                "rms_normalized_rmse_percent": 2.522830067915123,
                "reference_energy": 4.39402760061472,
                "candidate_energy": 4.394795159288737,
                "relative_energy_error_percent": 0.0174682260509613,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.516437684287666e-06,
                  "p90": 2.3367145331576467e-05,
                  "p95": 4.3219154372309065e-05,
                  "p99": 0.00019911152077838716,
                  "maximum": 0.0007001515477895737
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.041080983355641365,
                  "candidate": 0.04178113490343094
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": true
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.0656589644697784,
                "cvrmse_percent": 21.39522075553797,
                "rms_normalized_rmse_percent": 4.799270076044937,
                "reference_energy": 5.361717061637265,
                "candidate_energy": 5.358196613736794,
                "relative_energy_error_percent": 0.0656589644697784,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 3.403803566470742e-05,
                  "p99": 0.00015349641907959992,
                  "maximum": 0.0003934520063921809
                },
                "worst": {
                  "global_sensor_index": 82,
                  "local_sensor_index": 18,
                  "sky_patch_index": 154,
                  "rgb_channel": 0,
                  "reference": 0.0016215479699894786,
                  "candidate": 0.0012280959635972977
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.27668289358349785,
                "cvrmse_percent": 45.44812133498032,
                "rms_normalized_rmse_percent": 2.4925900012300812,
                "reference_energy": 4.1239500375942555,
                "candidate_energy": 4.112539773300302,
                "relative_energy_error_percent": 0.2766828935834978,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.009254633454475e-06,
                  "p90": 2.8647765020650695e-05,
                  "p95": 5.854523624293506e-05,
                  "p99": 0.0002274262980790806,
                  "maximum": 0.0009070746600627899
                },
                "worst": {
                  "global_sensor_index": 70,
                  "local_sensor_index": 6,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04514995403587818,
                  "candidate": 0.04424287937581539
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": -0.20961393852253435,
                "cvrmse_percent": 22.036510188009473,
                "rms_normalized_rmse_percent": 4.927267375108766,
                "reference_energy": 5.368086871293492,
                "candidate_energy": 5.356834612979263,
                "relative_energy_error_percent": 0.20961393852253438,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 4.3390180508140475e-05,
                  "p99": 0.00015652245201636084,
                  "maximum": 0.00048335292376577854
                },
                "worst": {
                  "global_sensor_index": 104,
                  "local_sensor_index": 16,
                  "sky_patch_index": 333,
                  "rgb_channel": 0,
                  "reference": 0.0020054515916854143,
                  "candidate": 0.002488804515451193
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": 0.3452691550444699,
                "cvrmse_percent": 47.72093771747375,
                "rms_normalized_rmse_percent": 2.6358192374639726,
                "reference_energy": 4.065290120198874,
                "candidate_energy": 4.079326313046991,
                "relative_energy_error_percent": 0.3452691550444699,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 6.147026113012544e-06,
                  "p90": 2.8998892958043143e-05,
                  "p95": 6.288127042353153e-05,
                  "p99": 0.00023749379906803355,
                  "maximum": 0.0008206851780414581
                },
                "worst": {
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.05959795415401459,
                  "candidate": 0.05877726897597313
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 303.68733301293105,
            "full": 8524.540332960896
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 426.6036249464378,
            "full": 12185.829708003439
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 409.48179189581424,
            "full": 11973.377624992281
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 298.44858299475163,
            "full": 8279.759375029244
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
            "identifier": "courtyard_rooms_west_grid",
            "start_sensor_index": 0,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.03251466340457438,
                "cvrmse_percent": 13.381082214534253,
                "rms_normalized_rmse_percent": 2.670984073280454,
                "reference_energy": 5.723136641367567,
                "candidate_energy": 5.724997499982692,
                "relative_energy_error_percent": 0.03251466340457438,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.130121381720525e-05,
                  "p99": 7.561119215097249e-05,
                  "maximum": 0.0002344854292459786
                },
                "worst": {
                  "global_sensor_index": 20,
                  "local_sensor_index": 20,
                  "sky_patch_index": 257,
                  "rgb_channel": 0,
                  "reference": 0.001914489024784416,
                  "candidate": 0.0021489744540303946
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.11239937226981883,
                "cvrmse_percent": 28.88081873273108,
                "rms_normalized_rmse_percent": 1.5132079593601513,
                "reference_energy": 4.386783204145665,
                "candidate_energy": 4.391713920929963,
                "relative_energy_error_percent": 0.11239937226981883,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.6792822584175155e-06,
                  "p90": 1.6347464224963915e-05,
                  "p95": 2.850705106993675e-05,
                  "p99": 0.00011292236129520335,
                  "maximum": 0.0006353314965963364
                },
                "worst": {
                  "global_sensor_index": 13,
                  "local_sensor_index": 13,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03677202947437763,
                  "candidate": 0.03740736097097397
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "start_sensor_index": 32,
            "sensor_count": 32,
            "stages": {
              "direct": {
                "nmbe_percent": 0.014537210409682609,
                "cvrmse_percent": 12.873435210635188,
                "rms_normalized_rmse_percent": 2.5700322819906947,
                "reference_energy": 5.726759705904293,
                "candidate_energy": 5.727592217012397,
                "relative_energy_error_percent": 0.014537210409682609,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 1.1199223808944155e-05,
                  "p99": 7.66832858789712e-05,
                  "maximum": 0.000181706651346758
                },
                "worst": {
                  "global_sensor_index": 45,
                  "local_sensor_index": 13,
                  "sky_patch_index": 171,
                  "rgb_channel": 0,
                  "reference": 0.0011115590459667146,
                  "candidate": 0.0009298523946199566
                },
                "passed": true,
                "energy_difference_negligible": true
              },
              "indirect": {
                "nmbe_percent": 0.20632820197832133,
                "cvrmse_percent": 29.156919972114327,
                "rms_normalized_rmse_percent": 1.5286492476983278,
                "reference_energy": 4.390948539539632,
                "candidate_energy": 4.400008304711058,
                "relative_energy_error_percent": 0.2063282019783213,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 3.6179037579131545e-06,
                  "p90": 1.616415465832688e-05,
                  "p95": 2.8664149408541032e-05,
                  "p99": 0.0001136009543552042,
                  "maximum": 0.0006549693644046783
                },
                "worst": {
                  "global_sensor_index": 44,
                  "local_sensor_index": 12,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04956699535250664,
                  "candidate": 0.050221964716911316
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "start_sensor_index": 64,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07043079113043951,
                "cvrmse_percent": 12.503689086190773,
                "rms_normalized_rmse_percent": 2.804975228999767,
                "reference_energy": 5.354773332566399,
                "candidate_energy": 5.358544741787767,
                "relative_energy_error_percent": 0.07043079113043951,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2500054910779e-05,
                  "p99": 8.368618437088995e-05,
                  "maximum": 0.00022285658633336425
                },
                "worst": {
                  "global_sensor_index": 71,
                  "local_sensor_index": 7,
                  "sky_patch_index": 259,
                  "rgb_channel": 0,
                  "reference": 0.00204298656899482,
                  "candidate": 0.0018201299826614559
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.14293632260191172,
                "cvrmse_percent": 27.427480780695404,
                "rms_normalized_rmse_percent": 1.5095923406082026,
                "reference_energy": 4.134997455106149,
                "candidate_energy": 4.129087041804137,
                "relative_energy_error_percent": 0.1429363226019117,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.596365720033191e-06,
                  "p90": 2.006506474572234e-05,
                  "p95": 3.8687569031026214e-05,
                  "p99": 0.0001282544311834495,
                  "maximum": 0.0006651598960161209
                },
                "worst": {
                  "global_sensor_index": 68,
                  "local_sensor_index": 4,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.03303574025630951,
                  "candidate": 0.03370090015232563
                },
                "passed": true,
                "negligible_relative_to_direct": false,
                "energy_difference_negligible": false
              }
            }
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "start_sensor_index": 88,
            "sensor_count": 24,
            "stages": {
              "direct": {
                "nmbe_percent": 0.07523732007902462,
                "cvrmse_percent": 13.143069694959756,
                "rms_normalized_rmse_percent": 2.9343465177901513,
                "reference_energy": 5.352481148479317,
                "candidate_energy": 5.356508211853168,
                "relative_energy_error_percent": 0.07523732007902462,
                "physically_near_zero": false,
                "rms_normalized_to": "stage",
                "absolute_error": {
                  "p50": 0.0,
                  "p90": 0.0,
                  "p95": 2.2577005438506603e-05,
                  "p99": 9.231048752553757e-05,
                  "maximum": 0.00022249750327318907
                },
                "worst": {
                  "global_sensor_index": 96,
                  "local_sensor_index": 8,
                  "sky_patch_index": 337,
                  "rgb_channel": 0,
                  "reference": 0.001771246490534395,
                  "candidate": 0.001548748987261206
                },
                "passed": true,
                "energy_difference_negligible": false
              },
              "indirect": {
                "nmbe_percent": -0.18074952606298011,
                "cvrmse_percent": 29.210071607195754,
                "rms_normalized_rmse_percent": 1.6214873429946162,
                "reference_energy": 4.08276963258238,
                "candidate_energy": 4.075390045821244,
                "relative_energy_error_percent": 0.1807495260629801,
                "physically_near_zero": false,
                "rms_normalized_to": "full",
                "absolute_error": {
                  "p50": 4.742276360047981e-06,
                  "p90": 2.0246030089765554e-05,
                  "p95": 4.0303508285433054e-05,
                  "p99": 0.0001355033979052677,
                  "maximum": 0.0006950348615646362
                },
                "worst": {
                  "global_sensor_index": 102,
                  "local_sensor_index": 14,
                  "sky_patch_index": 0,
                  "rgb_channel": 0,
                  "reference": 0.04461674951016903,
                  "candidate": 0.045311784371733665
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
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 508.0891669495031,
            "full": 17489.134708070196
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 738.438583095558,
            "full": 21593.300624983385
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 711.014625034295,
            "full": 15177.58799996227
          }
        },
        {
          "commands": [
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ],
            [
              "/usr/local/radiance/bin/rfluxmtx",
              "-I+",
              "-h",
              "-y",
              "112",
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
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome",
              "-i",
              "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct"
            ]
          ],
          "versions": {
            "rfluxmtx": "Usage: /usr/local/radiance/bin/rfluxmtx [-v][rcontrib options] sender.rad receiver.rad [-i system.oct] [system.rad ..]",
            "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
          },
          "timings_ms": {
            "direct": 572.2891250625253,
            "full": 15605.796040967107
          }
        }
      ]
    }
  ],
  "export_command": [
    "/usr/local/radiance/bin/oconv",
    "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.rad"
  ],
  "direct_oracles": [
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/direct_256/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/direct_256/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 256,
      "elapsed_ms": 14255.007207975723,
      "worker_pool_size": 12,
      "invocation_count": 7
    },
    {
      "commands": [
        [
          "/usr/local/radiance/bin/oconv",
          "-i",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/scene.oct",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/oracle/sky.dome"
        ],
        [
          "/usr/local/radiance/bin/rcontrib",
          "-h",
          "-w",
          "-ab",
          "0",
          "-M",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/direct_1024/sky_modifiers.txt",
          "-n",
          "1",
          "-fdd",
          "/Users/ssanjay/GitHub/foton/validation/results/2026-11-02-architectural-v4-metal-run2/courtyard_rooms/mf2/direct_1024/direct_scene.oct"
        ]
      ],
      "versions": {
        "oconv": "/usr/local/radiance/bin/oconv: fatal - unknown option: '-version'",
        "rcontrib": "RADIANCE 5.4a 2022-04-07 LBNL (5.4.b268408ad5)"
      },
      "sample_count": 1024,
      "elapsed_ms": 60107.29891702067,
      "worker_pool_size": 12,
      "invocation_count": 7
    }
  ],
  "coefficients": {
    "schema_version": 1,
    "passed": true,
    "matrix_shape": [
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16359535525576463,
            "cvrmse_percent": 5.954521378006722,
            "rms_normalized_rmse_percent": 1.1885696845537987,
            "reference_energy": 5.724825826156863,
            "candidate_energy": 5.715460277008788,
            "relative_energy_error_percent": 0.1635953552557685,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.174793139099947e-06,
              "p99": 2.9640955126523754e-05,
              "maximum": 0.00012478476855903864
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.001890760031528771,
              "candidate": 0.0020155448000878096,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.17816581276665636,
            "cvrmse_percent": 23.367357426846542,
            "rms_normalized_rmse_percent": 1.2242497772086762,
            "reference_energy": 4.388489832782648,
            "candidate_energy": 4.380671044203889,
            "relative_energy_error_percent": 0.1781658127666513,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.5461567904349067e-06,
              "p90": 1.389316821587272e-05,
              "p95": 2.108407411469668e-05,
              "p99": 5.2117614541202746e-05,
              "maximum": 0.0007625110447406769
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025134220719337463,
              "candidate": 0.024371709674596786,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.1699179409241966,
            "cvrmse_percent": 9.830612637529251,
            "rms_normalized_rmse_percent": 1.186914627028121,
            "reference_energy": 10.113315658939511,
            "candidate_energy": 10.096131321212678,
            "relative_energy_error_percent": 0.16991794092418783,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.5353809835214633e-06,
              "p90": 1.3491169738699682e-05,
              "p95": 1.9877944555446326e-05,
              "p99": 4.733825568109739e-05,
              "maximum": 0.0007625110447406769
            },
            "worst": {
              "global_sensor_index": 25,
              "local_sensor_index": 25,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.025134220719337463,
              "candidate": 0.024371709674596786,
              "position": [
                3.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.22728985327140036,
            "cvrmse_percent": 5.503560878086639,
            "rms_normalized_rmse_percent": 1.0991809066016618,
            "reference_energy": 5.7277349663760475,
            "candidate_energy": 5.714716405975196,
            "relative_energy_error_percent": 0.22728985327141585,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.5632256185633095e-06,
              "p99": 2.8286944143474102e-05,
              "maximum": 9.812612552195787e-05
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 11,
              "sky_patch_index": 221,
              "rgb_channel": 0,
              "reference": 0.001702859066426754,
              "candidate": 0.0016047329409047961,
              "position": [
                11.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.3890883143064832,
            "cvrmse_percent": 25.5089059858189,
            "rms_normalized_rmse_percent": 1.3373888602653,
            "reference_energy": 4.39491939621667,
            "candidate_energy": 4.377819278422801,
            "relative_energy_error_percent": 0.38908831430650337,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 3.4786739888659213e-06,
              "p90": 1.3964916433906183e-05,
              "p95": 2.079207570204742e-05,
              "p99": 5.3122243261896064e-05,
              "maximum": 0.0008415579795837402
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02959398739039898,
              "candidate": 0.02875242941081524,
              "position": [
                11.5,
                6.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.29753735646669477,
            "cvrmse_percent": 10.908691542516905,
            "rms_normalized_rmse_percent": 1.3172919069337559,
            "reference_energy": 10.122654362592716,
            "candidate_energy": 10.092535684397998,
            "relative_energy_error_percent": 0.297537356466686,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 3.464087512838887e-06,
              "p90": 1.3700569979846478e-05,
              "p95": 1.9698623873409747e-05,
              "p99": 4.881833243416564e-05,
              "maximum": 0.0008415579795837402
            },
            "worst": {
              "global_sensor_index": 41,
              "local_sensor_index": 9,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02959398739039898,
              "candidate": 0.02875242941081524,
              "position": [
                11.5,
                6.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2530179878625188,
            "cvrmse_percent": 5.308416089268609,
            "rms_normalized_rmse_percent": 1.1914820244588753,
            "reference_energy": 5.3573850143696164,
            "candidate_energy": 5.34382986660421,
            "relative_energy_error_percent": 0.25301798786252294,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.207738235592842e-06,
              "p99": 3.3115266705863073e-05,
              "maximum": 0.00013747472257819027
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 11,
              "sky_patch_index": 157,
              "rgb_channel": 0,
              "reference": 0.00013747472257819027,
              "candidate": 0.0,
              "position": [
                6.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": -0.9489797169214794,
            "cvrmse_percent": 33.198391197546606,
            "rms_normalized_rmse_percent": 1.8250794703551123,
            "reference_energy": 4.1313162649225985,
            "candidate_energy": 4.092110911526605,
            "relative_energy_error_percent": 0.9489797169214741,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.224043266276567e-06,
              "p90": 1.572470137034543e-05,
              "p95": 2.4449789634672925e-05,
              "p99": 6.098826997913394e-05,
              "maximum": 0.0011695511639118195
            },
            "worst": {
              "global_sensor_index": 78,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05360458046197891,
              "candidate": 0.05243502929806709,
              "position": [
                7.5,
                9.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": -0.5560350105713852,
            "cvrmse_percent": 14.326625272068666,
            "rms_normalized_rmse_percent": 1.8089517162326307,
            "reference_energy": 9.488701279292215,
            "candidate_energy": 9.435940778130815,
            "relative_energy_error_percent": 0.5560350105713852,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.1820389924396295e-06,
              "p90": 1.5284942492144182e-05,
              "p95": 2.2803465981269255e-05,
              "p99": 5.7247695804107876e-05,
              "maximum": 0.0011695511639118195
            },
            "worst": {
              "global_sensor_index": 78,
              "local_sensor_index": 14,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05360458046197891,
              "candidate": 0.05243502929806709,
              "position": [
                7.5,
                9.5,
                0.75
              ]
            },
            "passed": true
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.244312866791649,
            "cvrmse_percent": 5.594357095690952,
            "rms_normalized_rmse_percent": 1.2500904043879917,
            "reference_energy": 5.3575996305556846,
            "candidate_energy": 5.344510325307056,
            "relative_energy_error_percent": 0.24431286679164074,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.114147931337357e-06,
              "p99": 3.4202588722109795e-05,
              "maximum": 0.00013347197091206908
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 175,
              "rgb_channel": 0,
              "reference": 0.00013347197091206908,
              "candidate": 0.0,
              "position": [
                6.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 0.6873723986449817,
            "cvrmse_percent": 20.035271313639278,
            "rms_normalized_rmse_percent": 1.110907383508485,
            "reference_energy": 4.075974834341862,
            "candidate_energy": 4.103991960328843,
            "relative_energy_error_percent": 0.6873723986449708,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 4.26382530349656e-06,
              "p90": 1.6328227502526715e-05,
              "p95": 2.518598921597004e-05,
              "p99": 6.632801960222401e-05,
              "maximum": 0.000748801976442337
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05867548659443855,
              "candidate": 0.05942428857088089,
              "position": [
                6.5,
                -0.5,
                0.75
              ]
            },
            "passed": true,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 0.15824140461177993,
            "cvrmse_percent": 8.266290676734462,
            "rms_normalized_rmse_percent": 1.0608111750132938,
            "reference_energy": 9.433574464897546,
            "candidate_energy": 9.4485022856359,
            "relative_energy_error_percent": 0.15824140461179878,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 4.2448566546227084e-06,
              "p90": 1.5851197531446815e-05,
              "p95": 2.4255365133285522e-05,
              "p99": 5.576052935793965e-05,
              "maximum": 0.000748801976442337
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.05867548659443855,
              "candidate": 0.05942428857088089,
              "position": [
                6.5,
                -0.5,
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
      112,
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
        "identifier": "courtyard_rooms_west_grid",
        "full_identifier": "courtyard_rooms_west_grid",
        "start_sensor_index": 0,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.16359535525576463,
            "cvrmse_percent": 5.954521378006722,
            "rms_normalized_rmse_percent": 1.1885696845537987,
            "reference_energy": 5.724825826156863,
            "candidate_energy": 5.715460277008788,
            "relative_energy_error_percent": 0.1635953552557685,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 4.174793139099947e-06,
              "p99": 2.9640955126523754e-05,
              "maximum": 0.00012478476855903864
            },
            "worst": {
              "global_sensor_index": 18,
              "local_sensor_index": 18,
              "sky_patch_index": 257,
              "rgb_channel": 0,
              "reference": 0.001890760031528771,
              "candidate": 0.0020155448000878096,
              "position": [
                2.5,
                5.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 83.22809217856015,
            "cvrmse_percent": 990.541092406182,
            "rms_normalized_rmse_percent": 37.640151851672066,
            "reference_energy": 2.3908293712597413,
            "candidate_energy": 4.380671044203889,
            "relative_energy_error_percent": 83.22809217856015,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0245197245239979e-05,
              "p90": 5.6779997976263985e-05,
              "p95": 8.213197288569028e-05,
              "p99": 0.000165577832376584,
              "maximum": 0.013692248612642288
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02114853262901306,
              "candidate": 0.03484078124165535,
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
            "nmbe_percent": 24.403157546990194,
            "cvrmse_percent": 291.7987230593459,
            "rms_normalized_rmse_percent": 37.63892939246139,
            "reference_energy": 8.115655197416604,
            "candidate_energy": 10.096131321212678,
            "relative_energy_error_percent": 24.40315754699021,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.0200000360782724e-05,
              "p90": 5.64500005566515e-05,
              "p95": 8.222649994422676e-05,
              "p99": 0.00016327706282026966,
              "maximum": 0.013692248612642288
            },
            "worst": {
              "global_sensor_index": 4,
              "local_sensor_index": 4,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02114853262901306,
              "candidate": 0.03484078124165535,
              "position": [
                0.5,
                3.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "full_identifier": "courtyard_rooms_east_grid",
        "start_sensor_index": 32,
        "sensor_count": 32,
        "stages": {
          "direct": {
            "nmbe_percent": -0.22728985327140036,
            "cvrmse_percent": 5.503560878086639,
            "rms_normalized_rmse_percent": 1.0991809066016618,
            "reference_energy": 5.7277349663760475,
            "candidate_energy": 5.714716405975196,
            "relative_energy_error_percent": 0.22728985327141585,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 3.5632256185633095e-06,
              "p99": 2.8286944143474102e-05,
              "maximum": 9.812612552195787e-05
            },
            "worst": {
              "global_sensor_index": 43,
              "local_sensor_index": 11,
              "sky_patch_index": 221,
              "rgb_channel": 0,
              "reference": 0.001702859066426754,
              "candidate": 0.0016047329409047961,
              "position": [
                11.5,
                4.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 81.98301930526974,
            "cvrmse_percent": 971.9017702038469,
            "rms_normalized_rmse_percent": 36.98907669044793,
            "reference_energy": 2.405619653490402,
            "candidate_energy": 4.377819278422801,
            "relative_energy_error_percent": 81.98301930526974,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.0253173570617946e-05,
              "p90": 5.741999848396517e-05,
              "p95": 8.325930061801007e-05,
              "p99": 0.0001574694307055322,
              "maximum": 0.013383820652961731
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021265119314193726,
              "candidate": 0.03464893996715546,
              "position": [
                13.5,
                4.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 24.088228733394615,
            "cvrmse_percent": 287.43488612695364,
            "rms_normalized_rmse_percent": 36.98565720583477,
            "reference_energy": 8.133354619866449,
            "candidate_energy": 10.092535684397998,
            "relative_energy_error_percent": 24.088228733394626,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.022000014927471e-05,
              "p90": 5.700000110664405e-05,
              "p95": 8.163678357959719e-05,
              "p99": 0.00015586722176521922,
              "maximum": 0.013383820652961731
            },
            "worst": {
              "global_sensor_index": 59,
              "local_sensor_index": 27,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.021265119314193726,
              "candidate": 0.03464893996715546,
              "position": [
                13.5,
                4.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "full_identifier": "courtyard_rooms_north_grid",
        "start_sensor_index": 64,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.2530179878625188,
            "cvrmse_percent": 5.308416089268609,
            "rms_normalized_rmse_percent": 1.1914820244588753,
            "reference_energy": 5.3573850143696164,
            "candidate_energy": 5.34382986660421,
            "relative_energy_error_percent": 0.25301798786252294,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 7.207738235592842e-06,
              "p99": 3.3115266705863073e-05,
              "maximum": 0.00013747472257819027
            },
            "worst": {
              "global_sensor_index": 75,
              "local_sensor_index": 11,
              "sky_patch_index": 157,
              "rgb_channel": 0,
              "reference": 0.00013747472257819027,
              "candidate": 0.0,
              "position": [
                6.5,
                8.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 80.27280040599277,
            "cvrmse_percent": 977.7075800191902,
            "rms_normalized_rmse_percent": 40.736443235843275,
            "reference_energy": 2.2699547032668006,
            "candidate_energy": 4.092110911526605,
            "relative_energy_error_percent": 80.27280040599278,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.2110000170650892e-05,
              "p90": 6.68295833747834e-05,
              "p95": 9.970999963115901e-05,
              "p99": 0.00018726162961684055,
              "maximum": 0.01418938860297203
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022822242230176926,
              "candidate": 0.037011630833148956,
              "position": [
                6.5,
                11.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 23.712082160342703,
            "cvrmse_percent": 290.95073345241707,
            "rms_normalized_rmse_percent": 40.73328919424599,
            "reference_energy": 7.627339717636417,
            "candidate_energy": 9.435940778130815,
            "relative_energy_error_percent": 23.7120821603427,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.1974575386375363e-05,
              "p90": 6.569000106537715e-05,
              "p95": 9.868999768514186e-05,
              "p99": 0.00018639236222952585,
              "maximum": 0.01418938860297203
            },
            "worst": {
              "global_sensor_index": 72,
              "local_sensor_index": 8,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.022822242230176926,
              "candidate": 0.037011630833148956,
              "position": [
                6.5,
                11.5,
                0.75
              ]
            },
            "passed": false
          }
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "full_identifier": "courtyard_rooms_south_grid",
        "start_sensor_index": 88,
        "sensor_count": 24,
        "stages": {
          "direct": {
            "nmbe_percent": -0.244312866791649,
            "cvrmse_percent": 5.594357095690952,
            "rms_normalized_rmse_percent": 1.2500904043879917,
            "reference_energy": 5.3575996305556846,
            "candidate_energy": 5.344510325307056,
            "relative_energy_error_percent": 0.24431286679164074,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 0.0,
              "p90": 0.0,
              "p95": 8.114147931337357e-06,
              "p99": 3.4202588722109795e-05,
              "maximum": 0.00013347197091206908
            },
            "worst": {
              "global_sensor_index": 96,
              "local_sensor_index": 8,
              "sky_patch_index": 175,
              "rgb_channel": 0,
              "reference": 0.00013347197091206908,
              "candidate": 0.0,
              "position": [
                6.5,
                -0.5,
                0.75
              ]
            },
            "passed": true
          },
          "indirect": {
            "nmbe_percent": 86.86782291204118,
            "cvrmse_percent": 1080.6661981227,
            "rms_normalized_rmse_percent": 44.75526820513205,
            "reference_energy": 2.1962004460557103,
            "candidate_energy": 4.103991960328843,
            "relative_energy_error_percent": 86.86782291204116,
            "physically_near_zero": false,
            "rms_normalized_to": "full",
            "absolute_error": {
              "p50": 1.1705953216534226e-05,
              "p90": 7.553999603260309e-05,
              "p95": 0.00010070390999317169,
              "p99": 0.00019160368829034243,
              "maximum": 0.015801463276147842
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02106189727783203,
              "candidate": 0.036863360553979874,
              "position": [
                6.5,
                -3.5,
                0.75
              ]
            },
            "passed": false,
            "negligible_relative_to_direct": false
          },
          "full": {
            "nmbe_percent": 25.08276880256618,
            "cvrmse_percent": 314.1794263174514,
            "rms_normalized_rmse_percent": 44.75317481756638,
            "reference_energy": 7.553800076611395,
            "candidate_energy": 9.4485022856359,
            "relative_energy_error_percent": 25.0827688025662,
            "physically_near_zero": false,
            "rms_normalized_to": "stage",
            "absolute_error": {
              "p50": 1.168000017059967e-05,
              "p90": 7.473000005120412e-05,
              "p95": 9.97990491669043e-05,
              "p99": 0.0001905856421217321,
              "maximum": 0.015801463276147842
            },
            "worst": {
              "global_sensor_index": 99,
              "local_sensor_index": 11,
              "sky_patch_index": 0,
              "rgb_channel": 0,
              "reference": 0.02106189727783203,
              "candidate": 0.036863360553979874,
              "position": [
                6.5,
                -3.5,
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
      "bias_percent": 0.0026900182788565613,
      "rms_normalized_error_percent": 0.24459107471513675,
      "absolute_error": {
        "p95": 0.11974979875039192,
        "p99": 0.1523207317211236,
        "maximum": 0.15478000975630835
      },
      "worst_index": [
        104
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 14.547530800898524,
      "reference_fraction_of_uniform": 1.0,
      "rms_normalized_to_uniform_percent": 0.24459107471513675
    },
    "overcast": {
      "bias_percent": 0.03967108320146638,
      "rms_normalized_error_percent": 0.19588145806941507,
      "absolute_error": {
        "p95": 0.06520462036132811,
        "p99": 0.08991425514221192,
        "maximum": 0.10097885131835938
      },
      "worst_index": [
        104
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 10.111489295959473,
      "reference_fraction_of_uniform": 0.6950656771659851,
      "rms_normalized_to_uniform_percent": 0.14470621629795727
    },
    "horizon": {
      "bias_percent": -1.8328250004248294,
      "rms_normalized_error_percent": 5.617240698535142,
      "absolute_error": {
        "p95": 0.026827462773111415,
        "p99": 0.033312330014673555,
        "maximum": 0.03420461293830063
      },
      "worst_index": [
        100
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 0.2086703776701695,
      "reference_fraction_of_uniform": 0.014344040959671385,
      "rms_normalized_to_uniform_percent": 0.06185631384877908
    },
    "north": {
      "bias_percent": -0.034946756790468686,
      "rms_normalized_error_percent": 0.2750743096280116,
      "absolute_error": {
        "p95": 0.04317350387573242,
        "p99": 0.0708181667327881,
        "maximum": 0.07362747192382812
      },
      "worst_index": [
        96
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.8053715229034424,
      "reference_fraction_of_uniform": 0.2615819573402405,
      "rms_normalized_to_uniform_percent": 0.09333019082075342
    },
    "east": {
      "bias_percent": 0.04049907532042944,
      "rms_normalized_error_percent": 0.2707025076224001,
      "absolute_error": {
        "p95": 0.04424716234207151,
        "p99": 0.05895821332931519,
        "maximum": 0.08366012573242188
      },
      "worst_index": [
        11
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.6945912837982178,
      "reference_fraction_of_uniform": 0.25396689772605896,
      "rms_normalized_to_uniform_percent": 0.09071023491074011
    },
    "south": {
      "bias_percent": -0.03627450893559004,
      "rms_normalized_error_percent": 0.30374058916725255,
      "absolute_error": {
        "p95": 0.05697917938232422,
        "p99": 0.07130644321441651,
        "maximum": 0.08790969848632812
      },
      "worst_index": [
        79
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7152938842773438,
      "reference_fraction_of_uniform": 0.2553899884223938,
      "rms_normalized_to_uniform_percent": 0.10111020257758613
    },
    "west": {
      "bias_percent": -0.10124673206151133,
      "rms_normalized_error_percent": 0.2712531872690819,
      "absolute_error": {
        "p95": 0.043210077285766584,
        "p99": 0.05488288879394532,
        "maximum": 0.06647968292236328
      },
      "worst_index": [
        79
      ],
      "passed": true,
      "physically_near_zero": false,
      "negligible": false,
      "reference_mean": 3.7057254314422607,
      "reference_fraction_of_uniform": 0.25473225116729736,
      "rms_normalized_to_uniform_percent": 0.09099540308549431
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
        "identifier": "courtyard_rooms_west_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": 0.10428921327999932,
          "cvrmse_percent": 2.428076364612113,
          "absolute_error_percentiles_lux": {
            "p50": 3.092355728149414,
            "p90": 25.779260253906255,
            "p95": 39.709567260742176,
            "p99": 83.35028320312503
          },
          "maximum_absolute_error_lux": 341.609375,
          "worst": {
            "sensor_index": 27,
            "position": [
              3.5,
              4.5,
              0.75
            ],
            "hour_of_year": 2960.5,
            "foton_lux": 19698.908203125,
            "radiance_lux": 20040.517578125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.5595333904109584,
            "maximum_error_percentage_points": 2.60041095890411,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.19888553865612701,
            "maximum_error_percentage_points": 0.6196440964147243,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.22223030821917766,
            "maximum_error_percentage_points": 1.015479452054798,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.2252482876712334,
            "maximum_error_percentage_points": 1.015479452054798,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.010761986301369781,
            "maximum_error_percentage_points": 0.08136986301369831,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 34.375,
          "radiance_percent": 34.375,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_east_grid",
        "sensor_count": 32,
        "illuminance": {
          "nmbe_percent": 0.03147530321769163,
          "cvrmse_percent": 2.6125139492698435,
          "absolute_error_percentiles_lux": {
            "p50": 3.2440032958984375,
            "p90": 26.238195800781266,
            "p95": 40.226428222656224,
            "p99": 89.38641601562503
          },
          "maximum_absolute_error_lux": 275.3515625,
          "worst": {
            "sensor_index": 4,
            "position": [
              10.5,
              3.5,
              0.75
            ],
            "hour_of_year": 3518.5,
            "foton_lux": 34259.46875,
            "radiance_lux": 34534.8203125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.375042808219178,
            "maximum_error_percentage_points": 1.8313698630137,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.17503534535991694,
            "maximum_error_percentage_points": 0.6329118594894823,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.17257277397260246,
            "maximum_error_percentage_points": 0.5778082191780811,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.17129280821917714,
            "maximum_error_percentage_points": 0.5246575342465789,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01831763698630136,
            "maximum_error_percentage_points": 0.11328767123287697,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 43.75,
          "radiance_percent": 46.875,
          "difference_percentage_points": 3.125,
          "tolerance_percentage_points": 3.125,
          "ambiguous_sensor_count": 1,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_north_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": -0.09749613089425042,
          "cvrmse_percent": 2.0126223076608833,
          "absolute_error_percentiles_lux": {
            "p50": 4.314842224121094,
            "p90": 36.24793701171875,
            "p95": 56.809448242187415,
            "p99": 128.3644384765623
          },
          "maximum_absolute_error_lux": 570.44677734375,
          "worst": {
            "sensor_index": 11,
            "position": [
              6.5,
              8.5,
              0.75
            ],
            "hour_of_year": 1114.5,
            "foton_lux": 5586.7568359375,
            "radiance_lux": 6157.20361328125
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.14507420091324144,
            "maximum_error_percentage_points": 0.4912328767123313,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.07113910864071767,
            "maximum_error_percentage_points": 0.22027591416834014,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.05466894977168953,
            "maximum_error_percentage_points": 0.1916438356164356,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.05720890410959031,
            "maximum_error_percentage_points": 0.2217808219178039,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.01889840182648349,
            "maximum_error_percentage_points": 0.10602739726027366,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 87.5,
          "radiance_percent": 87.5,
          "difference_percentage_points": 0.0,
          "tolerance_percentage_points": 4.166666666666667,
          "ambiguous_sensor_count": 0,
          "ambiguity_band_percentage_points": 5.0,
          "unexplained_flip_percentage_points": 0.0,
          "passed": true
        }
      },
      {
        "identifier": "courtyard_rooms_south_grid",
        "sensor_count": 24,
        "illuminance": {
          "nmbe_percent": 0.16092789803413968,
          "cvrmse_percent": 3.7596431761674074,
          "absolute_error_percentiles_lux": {
            "p50": 2.867584228515625,
            "p90": 20.68610839843751,
            "p95": 30.31217041015624,
            "p99": 54.74525909423828
          },
          "maximum_absolute_error_lux": 162.2965087890625,
          "worst": {
            "sensor_index": 8,
            "position": [
              6.5,
              -0.5,
              0.75
            ],
            "hour_of_year": 4447.5,
            "foton_lux": 1568.330322265625,
            "radiance_lux": 1730.6268310546875
          },
          "physically_dark": false,
          "passed": true
        },
        "metrics": {
          "da": {
            "mean_absolute_error_percentage_points": 0.41687214611872064,
            "maximum_error_percentage_points": 1.5105479452054773,
            "passed": true
          },
          "cda": {
            "mean_absolute_error_percentage_points": 0.08231331886448483,
            "maximum_error_percentage_points": 0.23130946827799193,
            "passed": true
          },
          "udi_lower": {
            "mean_absolute_error_percentage_points": 0.07937785388127801,
            "maximum_error_percentage_points": 0.33191780821917405,
            "passed": true
          },
          "udi": {
            "mean_absolute_error_percentage_points": 0.07937785388128038,
            "maximum_error_percentage_points": 0.33191780821917405,
            "passed": true
          },
          "udi_upper": {
            "mean_absolute_error_percentage_points": 0.0,
            "maximum_error_percentage_points": 0.0,
            "passed": true
          }
        },
        "sda": {
          "foton_percent": 41.666666666666664,
          "radiance_percent": 41.666666666666664,
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
      "maximum_error_percentage_points": 0.0049464897260236285,
      "metrics": {
        "da": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849310097,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.0046575342465757785,
            "passed": true
          }
        ],
        "cda": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0049464897260236285,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004901005993161789,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004925620719177459,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004819937928090212,
            "passed": true
          }
        ],
        "udi": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849302991,
            "passed": true
          }
        ],
        "udi_lower": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
            "maximum_error_percentage_points": 0.004931506849317202,
            "passed": true
          }
        ],
        "udi_upper": [
          {
            "identifier": "courtyard_rooms_west_grid",
            "maximum_error_percentage_points": 0.0046575342465753344,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_east_grid",
            "maximum_error_percentage_points": 0.004520547945206843,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_north_grid",
            "maximum_error_percentage_points": 0.0039726027397266606,
            "passed": true
          },
          {
            "identifier": "courtyard_rooms_south_grid",
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
      "study_preparation_seconds": 0.02011658390983939,
      "weather_seconds": 0.12650733394548297,
      "metric_reduction_seconds": 0.3971075000008568,
      "write_seconds": 0.08856658299919218,
      "total_seconds": 0.6125705830054358,
      "cold_end_to_end_seconds": 0.6326871669152752,
      "warm_study_seconds": null,
      "raw_export_seconds": 0.043838041950948536,
      "engine_upload_seconds": 0.000921792,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.2803570416290313,
      "engine_annual_reduction_seconds": 0.004218750051222742,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.2803570416290313
    },
    "candidate_cached": {
      "study_preparation_seconds": 0.02011658390983939,
      "weather_seconds": 0.11041804205160588,
      "metric_reduction_seconds": 0.07078458298929036,
      "write_seconds": 0.0872418750077486,
      "total_seconds": 0.2687039580196142,
      "cold_end_to_end_seconds": null,
      "warm_study_seconds": 0.2687039580196142,
      "raw_export_seconds": 0.040190499974414706,
      "engine_upload_seconds": 0.000146875,
      "engine_acceleration_structure_seconds": 0.0,
      "engine_tracing_seconds": 0.0,
      "engine_annual_reduction_seconds": 0.004322875058278441,
      "engine_snapshot_seconds": 0.0,
      "coefficient_trace_seconds": 0.0
    },
    "coefficient_stages_seconds": {
      "direct": 0.015908416942693293,
      "full": 0.2726200830657035
    }
  },
  "elapsed_seconds": 237.60898074996658,
  "result_class": "passed"
}
```
