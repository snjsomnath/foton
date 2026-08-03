"""Convert Honeybee models into the native Foton scene contract."""

from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatch
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import numpy as np

OPAQUE_EXTERIOR_ACTIVE_MASK = (1 << 0) | (1 << 2) | (1 << 3)
CONTEXT_ROOM_ID = 0


@dataclass(frozen=True)
class PreparedHoneybeeScene:
    model: Any
    model_fingerprint: str
    arrays: dict[str, np.ndarray]
    grid_info: list[dict[str, Any]]
    room_map: dict[str, int]
    geometry_info: dict[str, Any]
    validation_warnings: tuple[dict[str, Any], ...]

    def create_native_scene(self, engine):
        return engine.create_scene(
            self.arrays["vertices"],
            self.arrays["triangles"],
            self.arrays["triangle_materials"],
            self.arrays["mesh_ranges"],
            self.arrays["instance_transforms"],
            self.arrays["instance_mesh_indices"],
            self.arrays["instance_room_ids"],
            self.arrays["instance_masks"],
            self.arrays["material_kinds"],
            self.arrays["material_diffuse_rgb"],
            self.arrays["material_transmittance_rgb"],
            self.arrays["sensor_positions"],
            self.arrays["sensor_normals"],
            self.arrays["sensor_ids"],
            self.arrays["sensor_room_ids"],
            self.arrays["sensor_area_weights"],
        )


def prepare_honeybee_scene(
    model_or_path,
    *,
    grid_filter="*",
    grid_size=0.5,
    sensor_height=0.75,
    include_aperture_glazing=False,
) -> PreparedHoneybeeScene:
    if not isinstance(grid_filter, str) or not grid_filter:
        raise ValueError("grid_filter must be a non-empty string")
    if not np.isfinite(grid_size) or grid_size <= 0:
        raise ValueError("grid_size must be finite and positive")
    if not np.isfinite(sensor_height) or sensor_height <= 0:
        raise ValueError("sensor_height must be finite and positive")

    model, validation_warnings = _load_and_normalize_model(model_or_path)
    _validate_supported_model(
        model, include_aperture_glazing=include_aperture_glazing
    )
    room_map = {
        room.identifier: index + 1 for index, room in enumerate(model.rooms)
    }
    if not room_map:
        raise ValueError("Honeybee model must contain at least one Room")

    geometry_arrays, geometry_info = _prepare_geometry(
        model,
        room_map,
        include_aperture_glazing=include_aperture_glazing,
    )
    sensor_arrays, grid_info = _prepare_sensors(
        model,
        room_map,
        grid_filter=grid_filter,
        grid_size=float(grid_size),
        sensor_height=float(sensor_height),
    )
    arrays = {
        **geometry_arrays,
        **sensor_arrays,
    }
    fingerprint = _fingerprint_model(
        model,
        grid_filter,
        grid_size,
        sensor_height,
        include_aperture_glazing,
    )
    return PreparedHoneybeeScene(
        model=model,
        model_fingerprint=fingerprint,
        arrays=arrays,
        grid_info=grid_info,
        room_map=room_map,
        geometry_info=geometry_info,
        validation_warnings=tuple(validation_warnings),
    )


def _load_and_normalize_model(model_or_path):
    try:
        from honeybee.model import Model
    except ImportError as error:
        raise ImportError(
            "Honeybee support requires honeybee-core; install "
            "'foton-daylight[honeybee]'"
        ) from error

    if isinstance(model_or_path, (str, Path)):
        model = Model.from_file(str(Path(model_or_path).expanduser().resolve()))
    elif isinstance(model_or_path, Model):
        model = model_or_path.duplicate()
    else:
        raise TypeError("model must be a honeybee.model.Model or an .hbjson path")

    if model.units != "Meters":
        model.convert_to_units("Meters")
    messages = model.check_all(
        raise_exception=False,
        detailed=True,
        all_ext_checks=False,
    )
    messages = messages if isinstance(messages, list) else []
    warnings = []
    fatal = []
    for message in messages:
        if isinstance(message, dict) and str(message.get("code")) == "000108":
            warnings.append(dict(message))
        else:
            fatal.append(message)
    if fatal:
        details = "; ".join(
            item.get("message", str(item)) if isinstance(item, dict) else str(item)
            for item in fatal
        )
        raise ValueError(f"Honeybee model validation failed: {details}")
    return model, warnings


def _validate_supported_model(model, *, include_aperture_glazing=False):
    if model.doors and not include_aperture_glazing:
        raise ValueError(
            "direct_visibility does not yet define door opening semantics; "
            "remove Doors or convert the intended opening to an Aperture"
        )
    if getattr(model, "orphaned_apertures", ()):
        raise ValueError("orphaned Apertures are not supported")

    for face in model.faces:
        if face.type.__class__.__name__.lower() == "airboundary":
            raise ValueError(
                f"AirBoundary face {face.identifier!r} is not supported"
            )

    radiance = _radiance_properties(model)
    if radiance is None:
        return
    for field in ("dynamic_subface_groups", "dynamic_shade_groups"):
        if tuple(getattr(radiance, field, ())):
            raise ValueError(
                f"{field} are not supported by the direct_visibility recipe"
            )
    if tuple(getattr(radiance, "bsdf_modifiers", ())):
        raise ValueError("BSDF modifiers are not supported by direct_visibility")
    for modifier in getattr(radiance, "modifiers", ()):
        modifier_type = modifier.__class__.__name__.lower()
        if modifier_type in {"trans", "bsdf", "absdf"}:
            raise ValueError(
                f"Radiance modifier {modifier.identifier!r} is not supported"
            )


def _prepare_geometry(model, room_map, *, include_aperture_glazing=False):
    groups: dict[int, list[tuple[Any, int]]] = {
        room_id: [] for room_id in room_map.values()
    }
    groups[CONTEXT_ROOM_ID] = []
    material_indices: dict[tuple[Any, ...], int] = {}
    material_kinds: list[int] = []
    material_diffuse_rgb: list[list[float]] = []
    material_transmittance_rgb: list[list[float]] = []
    material_info: list[dict[str, Any]] = []

    def material_index(obj) -> int:
        modifier = _resolved_modifier(obj)
        specification = _modifier_specification(modifier)
        key = (
            specification["kind"],
            *specification["diffuse_rgb"],
            *specification["transmittance_rgb"],
        )
        if key in material_indices:
            return material_indices[key]
        index = len(material_kinds)
        material_indices[key] = index
        material_kinds.append(int(specification["kind"]))
        material_diffuse_rgb.append(list(specification["diffuse_rgb"]))
        material_transmittance_rgb.append(
            list(specification["transmittance_rgb"])
        )
        material_info.append(
            {
                "index": index,
                "identifier": getattr(modifier, "identifier", f"material_{index}"),
                **specification,
            }
        )
        return index

    for room in model.rooms:
        room_id = room_map[room.identifier]
        for face in room.faces:
            groups[room_id].append(
                (face.punched_geometry, material_index(face))
            )
            if include_aperture_glazing:
                for subface in (*face.apertures, *face.doors):
                    groups[room_id].append(
                        (subface.geometry, material_index(subface))
                    )
    for face in model.orphaned_faces:
        groups[CONTEXT_ROOM_ID].append(
            (face.punched_geometry, material_index(face))
        )

    for shade in model.shades:
        room = _owning_room(shade)
        room_id = room_map.get(getattr(room, "identifier", ""), CONTEXT_ROOM_ID)
        groups[room_id].append(
            (shade.geometry, material_index(shade))
        )
    for shade_mesh in model.shade_meshes:
        groups[CONTEXT_ROOM_ID].append(
            (shade_mesh.geometry, material_index(shade_mesh))
        )

    vertices: list[list[float]] = []
    triangles: list[list[int]] = []
    triangle_materials: list[int] = []
    mesh_ranges: list[list[int]] = []
    instance_room_ids: list[int] = []
    triangle_counts: dict[str, int] = {}

    for room_id in [*room_map.values(), CONTEXT_ROOM_ID]:
        geometries = groups[room_id]
        if not geometries:
            continue
        first_triangle = len(triangles)
        for geometry, geometry_material_index in geometries:
            _append_geometry(
                geometry,
                vertices,
                triangles,
                triangle_materials,
                geometry_material_index,
            )
        triangle_count = len(triangles) - first_triangle
        if triangle_count == 0:
            continue
        mesh_ranges.append([first_triangle, triangle_count])
        instance_room_ids.append(room_id)
        label = (
            "context"
            if room_id == CONTEXT_ROOM_ID
            else next(key for key, value in room_map.items() if value == room_id)
        )
        triangle_counts[label] = triangle_count

    if not triangles:
        raise ValueError("Honeybee model did not produce any triangle geometry")

    instance_count = len(mesh_ranges)
    transforms = np.repeat(
        np.eye(4, dtype=np.float32)[None, :, :], instance_count, axis=0
    )
    arrays = {
        "vertices": np.ascontiguousarray(vertices, dtype=np.float32),
        "triangles": np.ascontiguousarray(triangles, dtype=np.uint32),
        "triangle_materials": np.ascontiguousarray(
            triangle_materials, dtype=np.uint32
        ),
        "mesh_ranges": np.ascontiguousarray(mesh_ranges, dtype=np.uint32),
        "instance_transforms": np.ascontiguousarray(transforms, dtype=np.float32),
        "instance_mesh_indices": np.arange(instance_count, dtype=np.uint32),
        "instance_room_ids": np.ascontiguousarray(
            instance_room_ids, dtype=np.uint32
        ),
        "instance_masks": np.full(
            instance_count, OPAQUE_EXTERIOR_ACTIVE_MASK, dtype=np.uint32
        ),
        "material_kinds": np.ascontiguousarray(
            material_kinds, dtype=np.uint32
        ),
        "material_diffuse_rgb": np.ascontiguousarray(
            material_diffuse_rgb, dtype=np.float32
        ),
        "material_transmittance_rgb": np.ascontiguousarray(
            material_transmittance_rgb, dtype=np.float32
        ),
    }
    info = {
        "vertex_count": len(vertices),
        "triangle_count": len(triangles),
        "instance_count": instance_count,
        "triangle_counts": triangle_counts,
        "aperture_mode": (
            "thin_glass" if include_aperture_glazing else "geometric_opening"
        ),
        "shade_mode": "opaque",
        "materials": material_info,
    }
    return arrays, info


def _append_geometry(
    geometry,
    vertices,
    triangles,
    triangle_materials,
    material_index=0,
):
    mesh = (
        geometry
        if geometry.__class__.__name__ == "Mesh3D"
        else geometry.triangulated_mesh3d
    )
    vertex_offset = len(vertices)
    vertices.extend(_xyz(vertex) for vertex in mesh.vertices)
    for face in mesh.faces:
        indices = [vertex_offset + int(index) for index in face]
        if len(indices) < 3:
            raise ValueError("Honeybee geometry contains a face with fewer than 3 vertices")
        for index in range(1, len(indices) - 1):
            triangles.append([indices[0], indices[index], indices[index + 1]])
            triangle_materials.append(int(material_index))


def _resolved_modifier(obj):
    try:
        modifier = obj.properties.radiance.modifier
    except (AttributeError, ImportError) as exc:
        raise ValueError(
            f"Honeybee object {getattr(obj, 'identifier', '<unknown>')!r} "
            "does not expose a resolved Radiance modifier"
        ) from exc
    if modifier is None:
        raise ValueError(
            f"Honeybee object {getattr(obj, 'identifier', '<unknown>')!r} "
            "has no resolved Radiance modifier"
        )
    return modifier


def _modifier_specification(modifier):
    modifier_type = modifier.__class__.__name__.lower()
    if modifier_type == "plastic":
        specularity = float(getattr(modifier, "specularity", 0.0))
        roughness = float(getattr(modifier, "roughness", 0.0))
        if abs(specularity) > 1.0e-9 or abs(roughness) > 1.0e-9:
            raise ValueError(
                f"Radiance Plastic modifier {modifier.identifier!r} has "
                "non-zero specularity or roughness; Foton v1 supports diffuse "
                "Plastic only"
            )
        diffuse = [
            float(modifier.r_reflectance),
            float(modifier.g_reflectance),
            float(modifier.b_reflectance),
        ]
        return {
            "kind": 0,
            "modifier_type": "Plastic",
            "diffuse_rgb": diffuse,
            "transmittance_rgb": [0.0, 0.0, 0.0],
        }
    if modifier_type == "glass":
        refraction_index = getattr(modifier, "refraction_index", None)
        if refraction_index is not None and not np.isclose(
            float(refraction_index), 1.52, atol=1.0e-6
        ):
            raise ValueError(
                f"Radiance Glass modifier {modifier.identifier!r} uses "
                f"refraction index {refraction_index}; Foton v1 supports 1.52"
            )
        transmittance = [
            float(modifier.r_transmittance),
            float(modifier.g_transmittance),
            float(modifier.b_transmittance),
        ]
        return {
            "kind": 1,
            "modifier_type": "Glass",
            "diffuse_rgb": [0.0, 0.0, 0.0],
            "transmittance_rgb": transmittance,
        }
    raise ValueError(
        f"Radiance modifier {modifier.identifier!r} of type "
        f"{modifier.__class__.__name__} is not supported by Foton v1"
    )


def _prepare_sensors(model, room_map, *, grid_filter, grid_size, sensor_height):
    radiance = _radiance_properties(model)
    embedded = tuple(getattr(radiance, "sensor_grids", ())) if radiance else ()
    embedded = tuple(
        grid
        for grid in embedded
        if fnmatch(getattr(grid, "full_identifier", grid.identifier), grid_filter)
        or fnmatch(grid.identifier, grid_filter)
    )

    sensor_positions: list[list[float]] = []
    sensor_normals: list[list[float]] = []
    sensor_room_ids: list[int] = []
    sensor_area_weights: list[float] = []
    grid_info: list[dict[str, Any]] = []

    if embedded:
        for grid in embedded:
            positions = list(grid.positions)
            directions = list(grid.directions)
            if len(positions) != len(directions):
                raise ValueError(
                    f"SensorGrid {grid.identifier!r} has inconsistent positions "
                    "and directions"
                )
            area_weights = _grid_area_weights(grid, len(positions))
            room_ids = _grid_room_ids(model, grid, positions, room_map)
            _append_sensor_grid(
                grid.identifier,
                getattr(grid, "full_identifier", grid.identifier),
                "embedded",
                positions,
                directions,
                room_ids,
                area_weights,
                sensor_positions,
                sensor_normals,
                sensor_room_ids,
                sensor_area_weights,
                grid_info,
            )
    else:
        for room in model.rooms:
            identifier = f"{room.identifier}_auto"
            if not fnmatch(identifier, grid_filter) and grid_filter != "*":
                continue
            mesh = room.generate_grid(grid_size, offset=sensor_height)
            if mesh is None or not mesh.faces:
                raise ValueError(
                    f"Room {room.identifier!r} produced an empty automatic sensor grid"
                )
            positions = list(mesh.face_centroids)
            directions = list(mesh.face_normals)
            area_weights = list(mesh.face_areas)
            room_ids = [room_map[room.identifier]] * len(positions)
            _append_sensor_grid(
                identifier,
                identifier,
                "automatic",
                positions,
                directions,
                room_ids,
                area_weights,
                sensor_positions,
                sensor_normals,
                sensor_room_ids,
                sensor_area_weights,
                grid_info,
            )

    if not sensor_positions:
        raise ValueError(
            f"no valid sensor grids matched grid_filter {grid_filter!r}"
        )
    arrays = {
        "sensor_positions": np.ascontiguousarray(
            sensor_positions, dtype=np.float32
        ),
        "sensor_normals": np.ascontiguousarray(sensor_normals, dtype=np.float32),
        "sensor_ids": np.arange(len(sensor_positions), dtype=np.uint32),
        "sensor_room_ids": np.ascontiguousarray(
            sensor_room_ids, dtype=np.uint32
        ),
        "sensor_area_weights": np.ascontiguousarray(
            sensor_area_weights, dtype=np.float32
        ),
    }
    return arrays, grid_info


def _append_sensor_grid(
    identifier,
    full_identifier,
    source,
    positions,
    directions,
    room_ids,
    area_weights,
    sensor_positions,
    sensor_normals,
    sensor_room_ids,
    sensor_area_weights,
    grid_info,
):
    if not positions:
        raise ValueError(f"SensorGrid {identifier!r} is empty")
    start = len(sensor_positions)
    for index, (position, direction, room_id, area_weight) in enumerate(
        zip(positions, directions, room_ids, area_weights, strict=True)
    ):
        position_values = np.asarray(_xyz(position), dtype=np.float64)
        direction_values = np.asarray(_xyz(direction), dtype=np.float64)
        length = float(np.linalg.norm(direction_values))
        if not np.isfinite(position_values).all():
            raise ValueError(
                f"SensorGrid {identifier!r} sensor {index} has a non-finite position"
            )
        if not np.isfinite(length) or length <= np.finfo(np.float32).eps:
            raise ValueError(
                f"SensorGrid {identifier!r} sensor {index} has a zero-length direction"
            )
        if not np.isfinite(area_weight) or area_weight <= 0:
            raise ValueError(
                f"SensorGrid {identifier!r} sensor {index} has an invalid area weight"
            )
        sensor_positions.append(position_values.tolist())
        sensor_normals.append((direction_values / length).tolist())
        sensor_room_ids.append(int(room_id))
        sensor_area_weights.append(float(area_weight))
    grid_info.append(
        {
            "identifier": identifier,
            "full_identifier": full_identifier,
            "source": source,
            "start_sensor_index": start,
            "sensor_count": len(positions),
            "room_ids": sorted(set(int(value) for value in room_ids)),
        }
    )


def _grid_area_weights(grid, sensor_count):
    mesh = getattr(grid, "mesh", None)
    if mesh is not None and len(mesh.face_areas) == sensor_count:
        return list(mesh.face_areas)
    return [1.0] * sensor_count


def _grid_room_ids(model, grid, positions, room_map):
    room_identifier = getattr(grid, "room_identifier", None)
    if room_identifier:
        if room_identifier not in room_map:
            raise ValueError(
                f"SensorGrid {grid.identifier!r} references unknown Room "
                f"{room_identifier!r}"
            )
        return [room_map[room_identifier]] * len(positions)

    room_ids = []
    for index, position in enumerate(positions):
        rooms = [
            room
            for room in model.rooms
            if room.geometry.is_point_inside(_point3d(position))
        ]
        if len(rooms) != 1:
            raise ValueError(
                f"SensorGrid {grid.identifier!r} sensor {index} must be enclosed "
                f"by exactly one Room; found {len(rooms)}"
            )
        room_ids.append(room_map[rooms[0].identifier])
    return room_ids


def _point3d(value):
    from ladybug_geometry.geometry3d.pointvector import Point3D

    x, y, z = _xyz(value)
    return Point3D(x, y, z)


def _xyz(value):
    if hasattr(value, "x"):
        return [float(value.x), float(value.y), float(value.z)]
    if len(value) != 3:
        raise ValueError("expected a three-component point or vector")
    return [float(value[0]), float(value[1]), float(value[2])]


def _owning_room(obj):
    current = getattr(obj, "parent", None)
    while current is not None:
        if current.__class__.__name__ == "Room":
            return current
        current = getattr(current, "parent", None)
    return None


def _radiance_properties(model):
    try:
        return model.properties.radiance
    except (AttributeError, ImportError):
        return None


def _fingerprint_model(
    model,
    grid_filter,
    grid_size,
    sensor_height,
    include_aperture_glazing,
):
    payload = {
        "model": model.to_dict(),
        "grid_filter": grid_filter,
        "grid_size": float(grid_size),
        "sensor_height": float(sensor_height),
        "include_aperture_glazing": bool(include_aperture_glazing),
        "adapter_schema": 2,
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return sha256(canonical).hexdigest()
