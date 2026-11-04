"""Extended, native-solver geometry used only by the cinematic demo."""
from __future__ import annotations

import math
import numpy as np
from pydantic import Field, model_validator

from .geometry import (
    GLASS_MATERIAL, SHADE_MATERIAL, WALL_MATERIAL, FLOOR_MATERIAL, CEILING_MATERIAL, ParametricScene,
    RoomParameters, _append_quad, generate_parametric_scene,
)


class DemoParameters(RoomParameters):
    """Room parameters for the animated demo: several windows, an L-shaped plan, more rooms and a facing building."""

    window_count: int = Field(1, ge=1, le=4)
    window_gap: float = Field(0.4, ge=0.1, le=3)
    rear_width_scale: float = Field(1.0, ge=0.5, le=1.5)
    room_count: int = Field(1, ge=1, le=1024)
    notch_width: float = Field(0.0, ge=0, le=40)
    notch_depth: float = Field(0.0, ge=0, le=40)
    context_height: float = Field(0.0, ge=0, le=30)
    context_offset: float = Field(0.0, ge=-25, le=25)
    context_distance: float = Field(4.0, ge=1, le=30)

    @model_validator(mode="after")
    def validate_demo(self):
        """Reject windows that do not fit the facade, a notch that leaves no room, and more than 30,000 sensors."""
        span = self.window_count * self.window_width + (self.window_count - 1) * self.window_gap
        if abs(self.window_offset) + span / 2 > self.width / 2 - 0.05:
            raise ValueError("all windows must fit within the facade with a 0.05 m side margin")
        sensors = math.ceil(self.width / self.sensor_spacing) * math.ceil(self.depth / self.sensor_spacing)
        if self.notch_width > self.width - 0.5 or self.notch_depth > self.depth - 0.5:
            raise ValueError("the L-shaped room must retain two wings at least 0.5 m wide")
        if sensors * self.room_count > 30_000:
            raise ValueError("the cinematic demo supports up to 30,000 sensors")
        return self


def generate_demo_scene(parameters: dict | DemoParameters) -> ParametricScene:
    """Build the demo's rooms, windows, shading and context building as a ``ParametricScene``."""
    p = parameters if isinstance(parameters, DemoParameters) else DemoParameters.model_validate(parameters)
    base = generate_parametric_scene(RoomParameters.model_validate(p.model_dump()))
    a = base.arrays
    vertices, triangles, materials = [], [], []
    has_notch = p.notch_width > 0 and p.notch_depth > 0
    cut_x, cut_y = p.width - p.notch_width, p.depth - p.notch_depth
    footprint = [(0, 0), (p.width, 0), (p.width, cut_y), (cut_x, cut_y), (cut_x, p.depth), (0, p.depth)] if has_notch else [(0, 0), (p.width, 0), (p.width, p.depth), (0, p.depth)]
    floor_rectangles = [(0, 0, p.width, cut_y), (0, cut_y, cut_x, p.depth)] if has_notch else [(0, 0, p.width, p.depth)]
    for x0, y0, x1, y1 in floor_rectangles:
        quad = ((x0, y0, 0), (x1, y0, 0), (x1, y1, 0), (x0, y1, 0))
        _append_quad(vertices, triangles, materials, quad, FLOOR_MATERIAL)
        _append_quad(vertices, triangles, materials, tuple((x, y, p.height) for x, y, _ in reversed(quad)), CEILING_MATERIAL)
    # Boundary walls only: no internal wall or overlapping floor through the L junction.
    for i in range(1, len(footprint)):
        x0, y0 = footprint[i]
        x1, y1 = footprint[(i + 1) % len(footprint)]
        _append_quad(vertices, triangles, materials, ((x0, y0, 0), (x1, y1, 0), (x1, y1, p.height), (x0, y0, p.height)), WALL_MATERIAL)
    span = p.window_count * p.window_width + (p.window_count - 1) * p.window_gap
    first = p.width / 2 + p.window_offset - span / 2
    z0, z1 = p.sill_height, p.sill_height + p.window_height
    last = 0.0
    for index in range(p.window_count):
        x0 = first + index * (p.window_width + p.window_gap)
        x1 = x0 + p.window_width
        for left, right, bottom, top in [(last, x0, 0, p.height), (x0, x1, 0, z0), (x0, x1, z1, p.height)]:
            _append_quad(vertices, triangles, materials,
                         ((left, 0, bottom), (right, 0, bottom), (right, 0, top), (left, 0, top)), WALL_MATERIAL)
        window = generate_parametric_scene(RoomParameters.model_validate({
            **p.model_dump(), "window_offset": (x0 + x1) / 2 - p.width / 2,
        })).arrays
        for triangle, material in zip(window["triangles"], window["triangle_materials"]):
            if material in (GLASS_MATERIAL, SHADE_MATERIAL):
                offset = len(vertices)
                vertices.extend(window["vertices"][triangle].tolist())
                triangles.append([offset, offset + 1, offset + 2])
                materials.append(int(material))
        last = x1
    _append_quad(vertices, triangles, materials,
                 ((last, 0, 0), (p.width, 0, 0), (p.width, 0, p.height), (last, 0, p.height)), WALL_MATERIAL)

    def taper(points):
        points = np.asarray(points, dtype=np.float32).copy()
        scale = 1 + (p.rear_width_scale - 1) * np.maximum(points[..., 1], 0) / p.depth
        points[..., 0] = p.width / 2 + (points[..., 0] - p.width / 2) * scale
        return points

    native_vertices = taper(vertices)
    native_triangles = np.asarray(triangles, dtype=np.uint32)
    wall_faces = np.asarray(materials) == WALL_MATERIAL
    native_triangles[wall_faces] = native_triangles[wall_faces, ::-1]
    grid = base.geometry_payload["grid"]
    # Split at the re-entrant corner so every cell is wholly inside the footprint.
    xs = sorted(set(np.linspace(0, p.width, grid["columns"] + 1).tolist() + ([cut_x] if has_notch else [])))
    ys = sorted(set(np.linspace(0, p.depth, grid["rows"] + 1).tolist() + ([cut_y] if has_notch else [])))
    local_cells = []
    for y0, y1 in zip(ys, ys[1:]):
        for x0, x1 in zip(xs, xs[1:]):
            if has_notch and x0 >= cut_x - 1e-7 and y0 >= cut_y - 1e-7:
                continue
            if x1 - x0 < 1e-6 or y1 - y0 < 1e-6:
                continue
            local_cells.append([(x0, y0, p.workplane_height), (x1, y0, p.workplane_height), (x1, y1, p.workplane_height), (x0, y1, p.workplane_height)])
    cells = taper(local_cells)
    local_sensors = cells.mean(axis=1)
    per_room = len(local_sensors)
    if per_room * p.room_count > 30_000:
        raise ValueError("the cinematic demo supports up to 30,000 sensors")
    local_areas = np.abs(np.sum(cells[:, :, 0] * np.roll(cells[:, :, 1], -1, axis=1) - cells[:, :, 1] * np.roll(cells[:, :, 0], -1, axis=1), axis=1)) * 0.5
    columns = min(p.room_count, math.ceil(math.sqrt(p.room_count) * 2))
    pitch_x = p.width * max(1, p.rear_width_scale) + 3
    pitch_y = p.depth + max(p.overhang_depth, p.left_fin_depth, p.right_fin_depth) + 3
    offsets = np.asarray([[(i % columns) * pitch_x, (i // columns) * pitch_y, 0] for i in range(p.room_count)], dtype=np.float32)
    transforms = np.tile(np.eye(4, dtype=np.float32), (p.room_count, 1, 1))
    transforms[:, :3, 3] = offsets
    a.update({
        "vertices": native_vertices,
        "triangles": native_triangles,
        "triangle_materials": np.asarray(materials, dtype=np.uint32),
        "mesh_ranges": np.asarray([[0, len(triangles)]], dtype=np.uint32),
        "instance_transforms": transforms,
        "instance_mesh_indices": np.zeros(p.room_count, dtype=np.uint32),
        "instance_room_ids": np.arange(1, p.room_count + 1, dtype=np.uint32),
        "instance_masks": np.repeat(a["instance_masks"], p.room_count),
        "sensor_positions": np.concatenate([local_sensors + offset for offset in offsets]),
        "sensor_normals": np.tile(np.asarray([[0, 0, 1]], dtype=np.float32), (per_room * p.room_count, 1)),
        "sensor_ids": np.arange(per_room * p.room_count, dtype=np.uint32),
        "sensor_room_ids": np.repeat(np.arange(1, p.room_count + 1, dtype=np.uint32), per_room),
        "sensor_area_weights": np.tile(local_areas, p.room_count),
    })
    # Context is a separate, real opaque mesh with no analysis sensors.
    context_vertices, context_triangles, context_materials = [], [], []
    if p.context_height > 0:
        for cx, width, depth, factor in [(p.width / 2, 5.5, 3.5, 1.0)]:
            x0, x1 = cx + p.context_offset - width / 2, cx + p.context_offset + width / 2
            y0, y1 = -p.context_distance - depth, -p.context_distance
            z = p.context_height * factor
            for face in [((x0,y0,0),(x1,y0,0),(x1,y1,0),(x0,y1,0)),
                         ((x0,y0,z),(x0,y1,z),(x1,y1,z),(x1,y0,z)),
                         ((x0,y0,0),(x0,y1,0),(x0,y1,z),(x0,y0,z)),
                         ((x1,y0,0),(x1,y0,z),(x1,y1,z),(x1,y1,0)),
                         ((x0,y0,0),(x0,y0,z),(x1,y0,z),(x1,y0,0)),
                         ((x0,y1,0),(x1,y1,0),(x1,y1,z),(x0,y1,z))]:
                _append_quad(context_vertices, context_triangles, context_materials, face, 5)
    room_vertex_count = len(native_vertices)
    if context_vertices:
        a["vertices"] = np.concatenate([native_vertices, np.asarray(context_vertices, dtype=np.float32)])
        a["triangles"] = np.concatenate([native_triangles, np.asarray(context_triangles, dtype=np.uint32) + room_vertex_count])
        a["triangle_materials"] = np.concatenate([a["triangle_materials"], np.asarray(context_materials, dtype=np.uint32)])
        a["mesh_ranges"] = np.asarray([[0, len(triangles)], [len(triangles), len(context_triangles)]], dtype=np.uint32)
        a["instance_transforms"] = np.concatenate([transforms, np.eye(4, dtype=np.float32)[None]])
        a["instance_mesh_indices"] = np.append(a["instance_mesh_indices"], np.uint32(1))
        a["instance_room_ids"] = np.append(a["instance_room_ids"], np.uint32(0))
        a["instance_masks"] = np.append(a["instance_masks"], a["instance_masks"][0])
    a["material_kinds"] = np.append(a["material_kinds"], np.uint32(0))
    a["material_diffuse_rgb"] = np.concatenate([a["material_diffuse_rgb"], np.asarray([[.35,.35,.35]], dtype=np.float32)])
    a["material_transmittance_rgb"] = np.concatenate([a["material_transmittance_rgb"], np.zeros((1,3), dtype=np.float32)])
    a = {key: np.ascontiguousarray(value) for key, value in a.items()}
    displayed_vertices = np.concatenate([native_vertices + offset for offset in offsets])
    displayed_triangles = np.concatenate([native_triangles + i * room_vertex_count for i in range(p.room_count)])
    displayed_materials = np.tile(materials, p.room_count)
    if context_vertices:
        displayed_triangles = np.concatenate([displayed_triangles, np.asarray(context_triangles) + len(displayed_vertices)])
        displayed_vertices = np.concatenate([displayed_vertices, np.asarray(context_vertices)])
        displayed_materials = np.concatenate([displayed_materials, context_materials])
    zone_bounds = [native_vertices.min(axis=0).tolist(), native_vertices.max(axis=0).tolist()]
    geometry = {**base.geometry_payload,
        "vertices": displayed_vertices.tolist(), "triangles": displayed_triangles.tolist(),
        "triangle_materials": displayed_materials.tolist(),
        "material_names": [*base.geometry_payload["material_names"], "context"],
        "sensor_positions": a["sensor_positions"].tolist(), "sensor_ids": a["sensor_ids"].tolist(),
        "sensor_area_weights": a["sensor_area_weights"].tolist(),
        "sensor_cells": np.concatenate([cells + offset for offset in offsets]).tolist(),
        "room_count": p.room_count, "zone_bounds": zone_bounds,
        "zone_offsets": offsets.tolist(), "context_present": bool(context_vertices),
    }
    return ParametricScene(p, a, geometry)
