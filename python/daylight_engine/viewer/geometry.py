"""Parametric shoebox geometry and sensor-grid generation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
from pydantic import BaseModel, Field, model_validator


MASK_OPAQUE = 1 << 0
MASK_GLAZING = 1 << 1
MASK_EXTERIOR = 1 << 2
MASK_ACTIVE_BATCH = 1 << 3
IDENTITY_TRANSFORM = np.eye(4, dtype=np.float32)

MATERIAL_NAMES = ("wall", "floor", "ceiling", "shade", "glass")
WALL_MATERIAL = 0
FLOOR_MATERIAL = 1
CEILING_MATERIAL = 2
SHADE_MATERIAL = 3
GLASS_MATERIAL = 4


class RoomParameters(BaseModel):
    width: float = Field(6.0, ge=1.0, le=50.0)
    depth: float = Field(9.0, ge=1.0, le=50.0)
    height: float = Field(3.0, ge=2.0, le=12.0)
    window_width: float = Field(3.0, ge=0.2, le=40.0)
    window_height: float = Field(1.5, ge=0.2, le=10.0)
    sill_height: float = Field(1.0, ge=0.05, le=10.0)
    window_offset: float = Field(0.0, ge=-20.0, le=20.0)
    glazing_enabled: bool = True
    glazing_transmittance: float = Field(0.6, ge=0.0, le=1.0)
    overhang_depth: float = Field(0.75, ge=0.0, le=5.0)
    left_fin_depth: float = Field(0.5, ge=0.0, le=5.0)
    right_fin_depth: float = Field(0.5, ge=0.0, le=5.0)
    wall_reflectance: float = Field(0.7, ge=0.0, le=0.95)
    floor_reflectance: float = Field(0.2, ge=0.0, le=0.95)
    ceiling_reflectance: float = Field(0.8, ge=0.0, le=0.95)
    shade_reflectance: float = Field(0.5, ge=0.0, le=0.95)
    sensor_spacing: float = Field(0.5, ge=0.1, le=3.0)
    workplane_height: float = Field(0.75, ge=0.05, le=10.0)

    @model_validator(mode="after")
    def validate_geometry(self) -> "RoomParameters":
        margin = 0.05
        center = self.width * 0.5 + self.window_offset
        window_min = center - self.window_width * 0.5
        window_max = center + self.window_width * 0.5
        if window_min < margin or window_max > self.width - margin:
            raise ValueError("window must fit within the south wall with a 0.05 m side margin")
        if self.sill_height + self.window_height > self.height - margin:
            raise ValueError("window must fit below the ceiling with a 0.05 m margin")
        if self.workplane_height >= self.height - margin:
            raise ValueError("workplane height must remain below the ceiling")
        return self


@dataclass(frozen=True)
class ParametricScene:
    parameters: RoomParameters
    arrays: dict[str, np.ndarray]
    geometry_payload: dict[str, Any]

    def create_native_scene(self, engine: Any) -> Any:
        arrays = self.arrays
        return engine.create_scene(
            arrays["vertices"],
            arrays["triangles"],
            arrays["triangle_materials"],
            arrays["mesh_ranges"],
            arrays["instance_transforms"],
            arrays["instance_mesh_indices"],
            arrays["instance_room_ids"],
            arrays["instance_masks"],
            arrays["material_kinds"],
            arrays["material_diffuse_rgb"],
            arrays["material_transmittance_rgb"],
            arrays["sensor_positions"],
            arrays["sensor_normals"],
            arrays["sensor_ids"],
            arrays["sensor_room_ids"],
            arrays["sensor_area_weights"],
        )


def _append_quad(
    vertices: list[list[float]],
    triangles: list[list[int]],
    materials: list[int],
    points: tuple[tuple[float, float, float], ...],
    material: int,
) -> None:
    offset = len(vertices)
    vertices.extend([list(point) for point in points])
    triangles.extend(
        (
            [offset, offset + 1, offset + 2],
            [offset, offset + 2, offset + 3],
        )
    )
    materials.extend((material, material))


def _window_bounds(parameters: RoomParameters) -> tuple[float, float, float, float]:
    center = parameters.width * 0.5 + parameters.window_offset
    x_min = center - parameters.window_width * 0.5
    x_max = center + parameters.window_width * 0.5
    z_min = parameters.sill_height
    z_max = parameters.sill_height + parameters.window_height
    return x_min, x_max, z_min, z_max


def generate_parametric_scene(
    parameters: RoomParameters | dict[str, Any] | None = None,
) -> ParametricScene:
    if parameters is None:
        parameters = RoomParameters()
    elif not isinstance(parameters, RoomParameters):
        parameters = RoomParameters.model_validate(parameters)

    width = parameters.width
    depth = parameters.depth
    height = parameters.height
    x_min, x_max, z_min, z_max = _window_bounds(parameters)
    vertices: list[list[float]] = []
    triangles: list[list[int]] = []
    triangle_materials: list[int] = []

    _append_quad(
        vertices,
        triangles,
        triangle_materials,
        ((0, 0, 0), (width, 0, 0), (width, depth, 0), (0, depth, 0)),
        FLOOR_MATERIAL,
    )
    _append_quad(
        vertices,
        triangles,
        triangle_materials,
        ((0, 0, height), (0, depth, height), (width, depth, height), (width, 0, height)),
        CEILING_MATERIAL,
    )
    _append_quad(
        vertices,
        triangles,
        triangle_materials,
        ((0, 0, 0), (0, depth, 0), (0, depth, height), (0, 0, height)),
        WALL_MATERIAL,
    )
    _append_quad(
        vertices,
        triangles,
        triangle_materials,
        ((width, 0, 0), (width, 0, height), (width, depth, height), (width, depth, 0)),
        WALL_MATERIAL,
    )
    _append_quad(
        vertices,
        triangles,
        triangle_materials,
        ((width, depth, 0), (0, depth, 0), (0, depth, height), (width, depth, height)),
        WALL_MATERIAL,
    )

    south_rectangles = (
        ((0, 0, 0), (x_min, 0, 0), (x_min, 0, height), (0, 0, height)),
        ((x_max, 0, 0), (width, 0, 0), (width, 0, height), (x_max, 0, height)),
        ((x_min, 0, 0), (x_max, 0, 0), (x_max, 0, z_min), (x_min, 0, z_min)),
        ((x_min, 0, z_max), (x_max, 0, z_max), (x_max, 0, height), (x_min, 0, height)),
    )
    for rectangle in south_rectangles:
        _append_quad(vertices, triangles, triangle_materials, rectangle, WALL_MATERIAL)

    if parameters.overhang_depth > 0:
        _append_quad(
            vertices,
            triangles,
            triangle_materials,
            (
                (x_min, 0, z_max),
                (x_max, 0, z_max),
                (x_max, -parameters.overhang_depth, z_max),
                (x_min, -parameters.overhang_depth, z_max),
            ),
            SHADE_MATERIAL,
        )
    if parameters.left_fin_depth > 0:
        _append_quad(
            vertices,
            triangles,
            triangle_materials,
            (
                (x_min, 0, z_min),
                (x_min, -parameters.left_fin_depth, z_min),
                (x_min, -parameters.left_fin_depth, z_max),
                (x_min, 0, z_max),
            ),
            SHADE_MATERIAL,
        )
    if parameters.right_fin_depth > 0:
        _append_quad(
            vertices,
            triangles,
            triangle_materials,
            (
                (x_max, 0, z_min),
                (x_max, 0, z_max),
                (x_max, -parameters.right_fin_depth, z_max),
                (x_max, -parameters.right_fin_depth, z_min),
            ),
            SHADE_MATERIAL,
        )
    if parameters.glazing_enabled:
        _append_quad(
            vertices,
            triangles,
            triangle_materials,
            (
                (x_min, 0, z_min),
                (x_max, 0, z_min),
                (x_max, 0, z_max),
                (x_min, 0, z_max),
            ),
            GLASS_MATERIAL,
        )

    count_x = max(1, int(np.ceil(width / parameters.sensor_spacing)))
    count_y = max(1, int(np.ceil(depth / parameters.sensor_spacing)))
    cell_width = width / count_x
    cell_depth = depth / count_y
    sensor_positions = np.asarray(
        [
            [
                (column + 0.5) * cell_width,
                (row + 0.5) * cell_depth,
                parameters.workplane_height,
            ]
            for row in range(count_y)
            for column in range(count_x)
        ],
        dtype=np.float32,
    )
    sensor_count = sensor_positions.shape[0]
    material_diffuse = np.asarray(
        [
            [parameters.wall_reflectance] * 3,
            [parameters.floor_reflectance] * 3,
            [parameters.ceiling_reflectance] * 3,
            [parameters.shade_reflectance] * 3,
            [0.0, 0.0, 0.0],
        ],
        dtype=np.float32,
    )
    material_transmittance = np.zeros((len(MATERIAL_NAMES), 3), dtype=np.float32)
    material_transmittance[GLASS_MATERIAL] = parameters.glazing_transmittance
    vertices_array = np.ascontiguousarray(vertices, dtype=np.float32)
    triangles_array = np.ascontiguousarray(triangles, dtype=np.uint32)
    triangle_materials_array = np.ascontiguousarray(triangle_materials, dtype=np.uint32)

    arrays = {
        "vertices": vertices_array,
        "triangles": triangles_array,
        "triangle_materials": triangle_materials_array,
        "mesh_ranges": np.ascontiguousarray([[0, len(triangles)]], dtype=np.uint32),
        "instance_transforms": np.ascontiguousarray([IDENTITY_TRANSFORM], dtype=np.float32),
        "instance_mesh_indices": np.ascontiguousarray([0], dtype=np.uint32),
        "instance_room_ids": np.ascontiguousarray([1], dtype=np.uint32),
        "instance_masks": np.ascontiguousarray(
            [MASK_OPAQUE | MASK_GLAZING | MASK_EXTERIOR | MASK_ACTIVE_BATCH],
            dtype=np.uint32,
        ),
        "material_kinds": np.ascontiguousarray([0, 0, 0, 0, 1], dtype=np.uint32),
        "material_diffuse_rgb": np.ascontiguousarray(material_diffuse),
        "material_transmittance_rgb": np.ascontiguousarray(material_transmittance),
        "sensor_positions": np.ascontiguousarray(sensor_positions),
        "sensor_normals": np.ascontiguousarray(
            np.tile([0.0, 0.0, 1.0], (sensor_count, 1)),
            dtype=np.float32,
        ),
        "sensor_ids": np.ascontiguousarray(np.arange(sensor_count), dtype=np.uint32),
        "sensor_room_ids": np.ascontiguousarray(
            np.ones(sensor_count, dtype=np.uint32)
        ),
        "sensor_area_weights": np.ascontiguousarray(
            np.full(sensor_count, cell_width * cell_depth),
            dtype=np.float32,
        ),
    }
    geometry_payload = {
        "vertices": vertices_array.tolist(),
        "triangles": triangles_array.tolist(),
        "triangle_materials": triangle_materials_array.tolist(),
        "material_names": list(MATERIAL_NAMES),
        "sensor_positions": sensor_positions.tolist(),
        "sensor_ids": arrays["sensor_ids"].tolist(),
        "sensor_area_weights": arrays["sensor_area_weights"].tolist(),
        "grid": {
            "columns": count_x,
            "rows": count_y,
            "cell_width": cell_width,
            "cell_depth": cell_depth,
        },
        "window": {
            "x_min": x_min,
            "x_max": x_max,
            "z_min": z_min,
            "z_max": z_max,
        },
    }
    return ParametricScene(parameters, arrays, geometry_payload)
