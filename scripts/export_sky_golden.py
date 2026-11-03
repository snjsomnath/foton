"""Export a small ``gendaymtx`` golden file for the built-in sky test.

Runs Radiance's ``gendaymtx -O0`` on the repository EPWs at Tregenza (MF:1)
and Reinhart MF:2 density, keeps a spread of sun-up hours from each, and
stores them with the WEA inputs so ``tests/python/test_builtin_sky.py`` can
compare Foton's Perez sky against the oracle on machines without Radiance.

Run from a checkout with ladybug-core and Radiance available:

    python scripts/export_sky_golden.py --output tests/fixtures/sky/gendaymtx-golden.npz
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import tempfile

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EPWS = ("gothenburg", "phoenix", "seattle")
HOURS_PER_DENSITY = {1: 48, 2: 24}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--output", type=Path, default=ROOT / "tests/fixtures/sky/gendaymtx-golden.npz"
    )
    parser.add_argument("--radiance-bin")
    args = parser.parse_args(argv)

    from ladybug.wea import Wea

    from foton.honeybee.weather import (
        SKY_ROWS,
        _radiance_environment,
        executable_version,
        parse_radiance_binary_matrix,
        resolve_gendaymtx,
        wea_irradiance_arrays,
        wea_site,
    )

    executable = resolve_gendaymtx(args.radiance_bin)
    payload: dict[str, np.ndarray] = {
        "gendaymtx_version": np.array(executable_version(executable)),
        "epws": np.array(EPWS),
    }
    for name in EPWS:
        wea = Wea.from_epw_file(str(ROOT / "epw" / f"{name}.epw"))
        direct, diffuse, hours = wea_irradiance_arrays(wea)
        payload[f"{name}/location"] = np.array(wea_site(wea), dtype=np.float64)
        payload[f"{name}/direct_normal"] = direct
        payload[f"{name}/diffuse_horizontal"] = diffuse
        payload[f"{name}/hour_of_year"] = hours
        with tempfile.TemporaryDirectory(prefix="foton-sky-golden-") as temporary:
            wea_path = Path(temporary) / "weather.wea"
            wea.write(str(wea_path))
            modifiers = Path(temporary) / "suns.mod"
            subprocess.run(
                [
                    str(executable), "-n", "-D", str(Path(temporary) / "sun.mtx"),
                    "-M", str(modifiers), "-O0", str(wea_path),
                ],
                check=True, capture_output=True, env=_radiance_environment(executable),
            )
            sun_up = np.zeros(len(hours), dtype=bool)
            for line in modifiers.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    sun_up[int(line.strip().split("solar", 1)[1]) // 60] = True
            payload[f"{name}/sun_up"] = sun_up
            for density, count in HOURS_PER_DENSITY.items():
                completed = subprocess.run(
                    [str(executable), "-m", str(density), "-of", "-O0", str(wea_path)],
                    check=True, capture_output=True, env=_radiance_environment(executable),
                )
                matrix = parse_radiance_binary_matrix(
                    completed.stdout, SKY_ROWS[density], len(hours)
                )
                lit = np.nonzero(matrix.max(axis=(0, 2)) > 1e-3)[0]
                chosen = lit[np.linspace(0, len(lit) - 1, count).round().astype(int)]
                payload[f"{name}/mf{density}/hours"] = chosen.astype(np.int32)
                payload[f"{name}/mf{density}/columns"] = np.ascontiguousarray(
                    matrix[:, chosen, :]
                )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.output, **payload)
    print(f"wrote {args.output} ({args.output.stat().st_size / 1024:.0f} KiB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
