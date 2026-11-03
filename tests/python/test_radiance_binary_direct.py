"""Binary direct-oracle transport must agree with the established ASCII path."""

import os

import numpy as np
import pytest

from foton.honeybee.adapter import prepare_honeybee_scene
from foton.honeybee.radiance import run_radiance_integrated_direct
from validation.oracle import export_scene, patch_samples
from validation.scenes import make_scene


@pytest.mark.parametrize("density", (1, 2))
@pytest.mark.parametrize("identifier", ("black_open", "plan_cross_circle"))
def test_binary_double_direct_agrees_with_ascii_oracle(tmp_path, density, identifier):
    radiance = os.environ.get("FOTON_RADIANCE_BIN")
    if not radiance:
        pytest.skip("Set FOTON_RADIANCE_BIN for real Radiance I/O parity")
    model = make_scene(identifier)
    prepared = prepare_honeybee_scene(
        model, include_aperture_glazing=identifier != "black_open"
    )
    octree, dome, _ = export_scene(
        model, tmp_path / "oracle", density, radiance, identifier == "black_open"
    )
    directions, weights = patch_samples(density, 64)
    runs = [
        run_radiance_integrated_direct(
            prepared.arrays["sensor_positions"][:4],
            prepared.arrays["sensor_normals"][:4],
            directions,
            weights,
            octree=octree,
            sky_dome=dome,
            work_directory=tmp_path / ("binary" if binary else "ascii"),
            radiance_bin=radiance,
            workers=4,
            binary_io=binary,
            sensor_chunk=1,
        )
        for binary in (False, True)
    ]
    np.testing.assert_allclose(
        runs[1].coefficients, runs[0].coefficients, rtol=5e-4, atol=1e-8
    )
    assert np.isfinite(runs[1].coefficients).all()
    assert "-fdd" in runs[1].commands[-1]
    assert "-fdd" not in runs[0].commands[-1]
    assert runs[0].sample_count == runs[1].sample_count == 64
    assert runs[0].invocation_count == runs[1].invocation_count == 4
    command = runs[1].commands[-1]
    assert command[command.index("-n") + 1] == "1"
