"""Foton (two-phase, patch sun) against the stock Honeybee annual-daylight
recipe (enhanced two-phase, explicit sun) for two teaching rooms under three
climates, at the recipe's default and at converged ambient parameters."""
import json
import shutil
from pathlib import Path

from honeybee.model import Model
from foton.honeybee import HoneybeeStudy
from foton.honeybee.validation import compare_annual_daylight

ROOT = Path("/Users/ssanjay/GitHub/foton")
RUN2 = ROOT / "validation/results/2026-11-02-architectural-v4-metal-run2"
SCRATCH = Path(__file__).resolve().parent.parent
STOCK = {"default": SCRATCH / "stock", "converged": SCRATCH / "stock_hi"}
OUT = SCRATCH / "sun_vs_stock"
rows = []
for scene in ("teaching_depth6", "teaching_depth10"):
    model = Model.from_hbjson(str(RUN2 / scene / "mf1/model.hbjson"))
    study = HoneybeeStudy(
        model, backend="metal", radiance_bin="/usr/local/radiance/bin",
        weather_cache=OUT / "weather_cache",
    )
    for climate in ("gothenburg", "phoenix", "seattle"):
        folder = OUT / scene / climate
        shutil.rmtree(folder, ignore_errors=True)
        study.annual_daylight(
            ROOT / f"epw/{climate}.epw", output_folder=folder,
            export_illuminance=True, quality="final", sky_density=1,
        )
        for label, root in STOCK.items():
            manifest = json.loads((root / f"{scene}_{climate}/reference_manifest.json").read_text())
            result = compare_annual_daylight(
                folder, manifest["project"], oracle="stock",
                output_folder=OUT / f"cmp_{scene}_{climate}_{label}",
            )
            g = result["grids"][0]
            il, m, s = g["illuminance"], g["metrics"], g["sda"]
            rows.append({
                "scene": scene, "climate": climate, "stock": label,
                "nmbe": il["nmbe_percent"], "cvrmse": il["cvrmse_percent"],
                "da_mae": m["da"]["mean_absolute_error_percentage_points"],
                "da_max": m["da"]["maximum_error_percentage_points"],
                "udi_mae": m["udi"]["mean_absolute_error_percentage_points"],
                "udi_upper_mae": m["udi_upper"]["mean_absolute_error_percentage_points"],
                "sda_foton": s["foton_percent"], "sda_stock": s["radiance_percent"],
                "stock_minutes": manifest["elapsed_seconds"] / 60,
            })
(OUT / "table.json").write_text(json.dumps(rows, indent=2))
print(f"{'scene':16s} {'climate':10s} {'stock':9s} {'NMBE%':>7s} {'CVRMSE%':>8s} {'DA mae':>7s} {'DA max':>7s} {'UDI mae':>8s} {'UDI>mae':>8s} {'sDA F':>6s} {'sDA S':>6s}")
for r in rows:
    print(f"{r['scene']:16s} {r['climate']:10s} {r['stock']:9s} {r['nmbe']:+7.2f} {r['cvrmse']:8.2f} {r['da_mae']:7.2f} {r['da_max']:7.2f} {r['udi_mae']:8.2f} {r['udi_upper_mae']:8.2f} {r['sda_foton']:6.1f} {r['sda_stock']:6.1f}")
