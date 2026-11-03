"""Deterministic architectural daylight fixtures; all dimensions are metres.

Export HBJSON samples: ``python -m validation.scenes --output samples``.
Only diffuse Plastic and thin Glass are used; context is explicit opaque geometry.
"""

from dataclasses import asdict, dataclass
from pathlib import Path

_LEGACY_IDS = (
    "sealed",
    "black_open",
    "coloured_glass",
    "overhang_fins",
    "deep_reflective",
    "rooflit",
    "context_obstruction",
    "interior_glazing",
    "irregular",
    "acceptance",
)
SCENE_VERSION = 4

# Parameter sweeps a daylighting course actually varies. Each scene changes one
# thing against the 6 x 6 x 3 m, 0.5-reflectance, 3 x 1.5 m south-window base
# (which is `teaching_depth6`). Values are (room w, d, h), window (w, h, sill),
# opaque reflectance, overhang depth, obstruction angle in degrees.
TEACHING_BASE = {
    "room": (6, 6, 3),
    "window": (3.0, 1.5, 0.8),
    "reflectance": 0.5,
    "overhang": 0.0,
    "obstruction": 0,
}
TEACHING_SCENES = {
    # Window-to-wall ratio on an 18 m2 south wall; width fixed at 5.4 m.
    "teaching_wwr20": {"window": (5.4, 0.667, 0.8)},
    "teaching_wwr40": {"window": (5.4, 1.333, 0.8)},
    "teaching_wwr60": {"window": (5.4, 2.0, 0.8)},
    "teaching_depth4": {"room": (6, 4, 3)},
    "teaching_depth6": {},
    "teaching_depth8": {"room": (6, 8, 3)},
    "teaching_depth10": {"room": (6, 10, 3)},
    "teaching_reflectance30": {"reflectance": 0.3},
    "teaching_reflectance70": {"reflectance": 0.7},
    "teaching_overhang050": {"overhang": 0.5},
    "teaching_overhang100": {"overhang": 1.0},
    "teaching_obstruction30": {"obstruction": 30},
    "teaching_obstruction60": {"obstruction": 60},
    "teaching_classroom": {"room": (9, 7, 3.2), "window": (2.4, 1.6, 0.9), "windows": 3},
    "teaching_office": {"room": (12, 8, 2.8), "window": (11.0, 1.6, 0.9)},
    "teaching_living_room": {"room": (5, 4.5, 2.6), "window": (2.4, 2.0, 0.4)},
}
TEACHING_QUESTIONS = {
    "teaching_wwr20": "How does a 20% window-to-wall ratio light the base room?",
    "teaching_wwr40": "How does a 40% window-to-wall ratio light the base room?",
    "teaching_wwr60": "How does a 60% window-to-wall ratio light the base room?",
    "teaching_depth4": "How does daylight fall off in a 4 m deep room?",
    "teaching_depth6": "What is the 6 m deep teaching base room?",
    "teaching_depth8": "How does daylight fall off in an 8 m deep room?",
    "teaching_depth10": "How does daylight fall off in a 10 m deep room?",
    "teaching_reflectance30": "How much does 0.3 surface reflectance cost at the back of the room?",
    "teaching_reflectance70": "How much does 0.7 surface reflectance add at the back of the room?",
    "teaching_overhang050": "What does a 0.5 m overhang remove from the base room?",
    "teaching_overhang100": "What does a 1.0 m overhang remove from the base room?",
    "teaching_obstruction30": "How does a 30 degree obstruction angle reduce sky access?",
    "teaching_obstruction60": "How does a 60 degree obstruction angle reduce sky access?",
    "teaching_classroom": "How is a 9 x 7 m classroom with three windows lit?",
    "teaching_office": "How is a 12 x 8 m open-plan office with a ribbon window lit?",
    "teaching_living_room": "How is a 5 x 4.5 m living room with a tall window lit?",
}


def teaching_parameters(identifier):
    return {**TEACHING_BASE, **TEACHING_SCENES[identifier]}

# Exterior outlines of the specified rectangle unions, counter-clockwise.
PLAN_FOOTPRINTS = {
    "i": (
        (0, 0),
        (12, 0),
        (12, 3),
        (7.5, 3),
        (7.5, 9),
        (12, 9),
        (12, 12),
        (0, 12),
        (0, 9),
        (4.5, 9),
        (4.5, 3),
        (0, 3),
    ),
    "j": ((0, 0), (9, 0), (9, 12), (6, 12), (6, 3), (3, 3), (3, 6), (0, 6)),
    "l": ((0, 0), (9, 0), (9, 3), (3, 3), (3, 12), (0, 12)),
    "t": ((4.5, 0), (7.5, 0), (7.5, 9), (12, 9), (12, 12), (0, 12), (0, 9), (4.5, 9)),
    "cross": (
        (4.5, 0),
        (7.5, 0),
        (7.5, 4.5),
        (12, 4.5),
        (12, 7.5),
        (7.5, 7.5),
        (7.5, 12),
        (4.5, 12),
        (4.5, 7.5),
        (0, 7.5),
        (0, 4.5),
        (4.5, 4.5),
    ),
}
WINDOW_PROFILES = (
    "small_center",
    "large_center",
    "offset_low",
    "offset_high",
    "triangle",
    "circle",
    "arch",
    "distributed",
)


def _legacy_scene(identifier, repository):
    from honeybee.model import Model
    from honeybee.room import Room
    from honeybee.shade import Shade
    from honeybee_radiance.modifier.material import Plastic, Glass
    from honeybee_radiance.sensorgrid import SensorGrid
    from ladybug_geometry.geometry3d import Point3D, Face3D, Polyface3D

    if identifier not in SCENE_IDS:
        raise ValueError("Unknown validation scene: " + identifier)
    if identifier == "acceptance":
        return Model.from_hbjson(str(Path(repository) / "test_models/test.hbjson"))
    room = Room.from_box(identifier, 6, 12 if identifier == "deep_reflective" else 6, 3)
    if identifier == "irregular":
        footprint = Face3D(
            tuple(
                Point3D(x, y, 0)
                for x, y in ((0, 0), (6, 0), (6, 3), (3, 3), (3, 6), (0, 6))
            )
        )
        room = Room.from_polyface3d(
            identifier, Polyface3D.from_offset_face(footprint, 3)
        )
    rooms = [room]
    if identifier not in ("sealed", "rooflit"):
        wall = next(face for face in room.faces if face.normal.y < -0.9)
        aperture = wall.aperture_by_width_height(2, 1.5, 0.8)
        if identifier == "overhang_fins":
            aperture.overhang(0.9)
            for x in (2, 4):
                aperture.add_outdoor_shade(
                    Shade(
                        "fin_%s" % x,
                        Face3D(
                            tuple(
                                Point3D(*p)
                                for p in (
                                    (x, 0, 0.8),
                                    (x, -1, 0.8),
                                    (x, -1, 2.3),
                                    (x, 0, 2.3),
                                )
                            )
                        ),
                    )
                )
    if identifier == "rooflit":
        next(face for face in room.faces if face.normal.z > 0.9).apertures_by_ratio(0.2)
    if identifier == "interior_glazing":
        second = Room.from_box("adjacent", 6, 6, 3, origin=Point3D(6, 0, 0))
        for item, sign in ((room, 1), (second, -1)):
            next(
                face for face in item.faces if face.normal.x * sign > 0.9
            ).aperture_by_width_height(2, 1.5, 0.8)
        rooms.append(second)
        Room.solve_adjacency(rooms)
    model = Model(identifier, rooms)
    if identifier == "context_obstruction":
        model.add_shade(
            Shade(
                "neighbour",
                Face3D(
                    tuple(
                        Point3D(*p)
                        for p in ((-2, -2, 0), (8, -2, 0), (8, -2, 5), (-2, -2, 5))
                    )
                ),
            )
        )
    reflectance = (
        0
        if identifier == "black_open"
        else 0.85
        if identifier == "deep_reflective"
        else 0.5
    )
    opaque = Plastic.from_single_reflectance("diffuse", reflectance)
    glass = (
        Glass("coloured", 0.7, 0.6, 0.5)
        if identifier == "coloured_glass"
        else Glass.from_single_transmittance("clear", 0.6)
    )
    for face in model.faces:
        face.properties.radiance.modifier = opaque
    for aperture in model.apertures:
        aperture.properties.radiance.modifier = glass
    for item in rooms:
        grid = SensorGrid.from_mesh3d(
            item.identifier + "_grid", item.generate_grid(1, offset=0.75)
        )
        grid.room_identifier = item.identifier
        model.properties.radiance.add_sensor_grid(grid)
    return model


@dataclass(frozen=True)
class SceneSpec:
    identifier: str
    category: str
    question: str
    interactions: tuple[str, ...]
    room_count: int = 1
    include_glazing: bool = True
    footprint_family: str | None = None
    window_profile: str | None = None


# Original identifiers and geometry are retained for diagnostic continuity.
SCENE_SPECS = (
    SceneSpec(
        "sealed",
        "controls",
        "Does a completely enclosed room remain dark?",
        ("light_leaks",),
    ),
    SceneSpec(
        "black_open",
        "controls",
        "Is direct sky integration correct without glazing or reflections?",
        ("open_aperture", "direct_sky"),
        include_glazing=False,
    ),
    SceneSpec(
        "coloured_glass",
        "materials",
        "Does tinted glass preserve RGB transport and photopic conversion?",
        ("spectral_glazing", "multiple_bounces"),
    ),
    SceneSpec(
        "overhang_fins",
        "shading",
        "How do combined overhangs and side fins mask the sky?",
        ("overhang", "fins", "combined_shading"),
    ),
    SceneSpec(
        "deep_reflective",
        "materials",
        "Does reflected light reach the rear of a deep bright room?",
        ("deep_plan", "multiple_bounces", "high_reflectance"),
    ),
    SceneSpec(
        "rooflit",
        "openings",
        "How does a roof opening illuminate the workplane?",
        ("roof_glazing", "zenith_sky"),
    ),
    SceneSpec(
        "context_obstruction",
        "context",
        "How much sky does a neighbouring facade obstruct?",
        ("external_obstruction", "horizon_sky"),
    ),
    SceneSpec(
        "interior_glazing",
        "connections",
        "Does daylight pass through a shared glazed wall exactly once?",
        ("borrowed_light", "paired_apertures", "room_isolation"),
        2,
    ),
    SceneSpec(
        "irregular",
        "form",
        "Is an L-shaped room triangulated without filling its recess?",
        ("concave_plan", "self_occlusion"),
    ),
    SceneSpec(
        "acceptance",
        "integration",
        "Does the classroom and two-office model retain its Honeybee results?",
        ("real_hbjson", "grid_order", "sealed_zone", "stock_recipe"),
        3,
    ),
    SceneSpec(
        "side_lit_reference",
        "controls",
        "What is the clear-glazed south-facing reference room?",
        ("side_glazing", "baseline"),
    ),
    SceneSpec(
        "shallow_plan",
        "form",
        "How evenly does side lighting illuminate a shallow room?",
        ("shallow_plan", "daylight_penetration"),
    ),
    SceneSpec(
        "narrow_corridor",
        "form",
        "How far does end-window light travel down a narrow corridor?",
        ("deep_plan", "end_lighting"),
    ),
    SceneSpec(
        "double_height",
        "form",
        "How does tall glazing light a double-height volume?",
        ("tall_volume", "high_glazing"),
    ),
    SceneSpec(
        "pitched_roof",
        "form",
        "Do sloped roof surfaces reflect light correctly beneath a ridge?",
        ("sloped_faces", "nonrectangular_faces"),
    ),
    SceneSpec(
        "trapezoid_plan",
        "form",
        "How do splayed walls change illumination and reflections?",
        ("angled_walls", "nonorthogonal_plan"),
    ),
    SceneSpec(
        "u_shaped_plan",
        "form",
        "Do the wings of a U-shaped room occlude one another?",
        ("concave_plan", "self_occlusion", "multiple_openings"),
    ),
    SceneSpec(
        "north_facing",
        "orientation",
        "Is north-facing glazing assigned to the correct sky patches?",
        ("north_glazing", "sky_patch_order"),
    ),
    SceneSpec(
        "east_facing",
        "orientation",
        "Is east-facing glazing assigned to the correct sky patches?",
        ("east_glazing", "sky_patch_order"),
    ),
    SceneSpec(
        "west_facing",
        "orientation",
        "Is west-facing glazing assigned to the correct sky patches?",
        ("west_glazing", "sky_patch_order"),
    ),
    SceneSpec(
        "rotated_37",
        "orientation",
        "Does an oblique room retain its glazing, shades and grids?",
        ("oblique_orientation", "transformed_shades", "transformed_sensors"),
    ),
    SceneSpec(
        "corner_glazing",
        "openings",
        "How do windows on adjacent facades combine at a corner?",
        ("two_aspects", "corner_lighting"),
    ),
    SceneSpec(
        "opposite_glazing",
        "openings",
        "How does glazing on opposite facades balance daylight?",
        ("two_aspects", "bilateral_lighting"),
    ),
    SceneSpec(
        "ribbon_windows",
        "openings",
        "Do separated ribbon openings retain their opaque mullion gaps?",
        ("multiple_openings", "punched_faces", "mullion_gaps"),
    ),
    SceneSpec(
        "clerestory",
        "openings",
        "How does a high narrow opening distribute light toward the ceiling?",
        ("high_glazing", "ceiling_reflection"),
    ),
    SceneSpec(
        "full_height_glazing",
        "openings",
        "Is large near-floor glazing represented without edge leaks?",
        ("large_opening", "near_floor_glazing"),
    ),
    SceneSpec(
        "multiple_rooflights",
        "openings",
        "How do four separated rooflights combine across the workplane?",
        ("roof_glazing", "multiple_openings", "punched_roof"),
    ),
    SceneSpec(
        "rooflight_well",
        "shading",
        "How does a one-metre-deep opaque shaft below a rooflight restrict the sky?",
        ("roof_glazing", "interior_shades", "lightwell"),
    ),
    SceneSpec(
        "deep_overhang",
        "shading",
        "How does a deep overhang exclude high sky while retaining low sky?",
        ("overhang", "zenith_mask"),
    ),
    SceneSpec(
        "asymmetric_fins",
        "shading",
        "Do unequal fins produce different east and west sky masks?",
        ("fins", "asymmetric_shading"),
    ),
    SceneSpec(
        "horizontal_louvres",
        "shading",
        "Do repeated tilted horizontal blades preserve narrow sky gaps?",
        ("louvres", "tilted_shades", "small_gaps"),
    ),
    SceneSpec(
        "vertical_louvres",
        "shading",
        "How do repeated vertical blades screen oblique sky directions?",
        ("louvres", "azimuth_mask", "small_gaps"),
    ),
    SceneSpec(
        "eggcrate",
        "shading",
        "How do intersecting vertical and horizontal blades combine?",
        ("louvres", "combined_shading", "small_gaps"),
    ),
    SceneSpec(
        "light_shelf",
        "shading",
        "Does a shelf block direct light and reflect light toward the ceiling?",
        ("interior_shades", "exterior_shades", "shelf_reflection"),
    ),
    SceneSpec(
        "balcony_above",
        "shading",
        "How does an upper balcony slab shade a full-width facade?",
        ("balcony", "overhang", "context_occlusion"),
    ),
    SceneSpec(
        "recessed_window",
        "shading",
        "How do deep opaque window reveals screen low and oblique sky?",
        ("window_reveals", "combined_shading"),
    ),
    SceneSpec(
        "urban_canyon",
        "context",
        "How do tall buildings on both sides restrict side lighting?",
        ("closed_context", "urban_canyon", "horizon_mask"),
    ),
    SceneSpec(
        "courtyard_context",
        "context",
        "How does enclosing context restrict a room's courtyard view?",
        ("closed_context", "courtyard", "multiple_obstructions"),
    ),
    SceneSpec(
        "offset_tower",
        "context",
        "Does an off-axis tall obstruction affect the appropriate sky sectors?",
        ("closed_context", "asymmetric_obstruction", "height_contrast"),
    ),
    SceneSpec(
        "reflective_neighbour",
        "context",
        "Does a bright neighbouring facade contribute reflected daylight?",
        ("external_obstruction", "context_reflection", "high_reflectance"),
    ),
    SceneSpec(
        "dark_interior",
        "materials",
        "How does a dark finish suppress indirect illumination?",
        ("low_reflectance", "direct_indirect_separation"),
    ),
    SceneSpec(
        "bright_ceiling",
        "materials",
        "How much does changing only ceiling reflectance redistribute light?",
        ("ceiling_reflection", "surface_specific_materials"),
    ),
    SceneSpec(
        "coloured_walls",
        "materials",
        "Do coloured diffuse walls preserve RGB reflected transport?",
        ("spectral_reflection", "surface_specific_materials"),
    ),
    SceneSpec(
        "low_transmittance",
        "materials",
        "Does low-transmittance glass attenuate light without turning opaque?",
        ("glazing_attenuation",),
    ),
    SceneSpec(
        "mixed_glazing",
        "materials",
        "Are adjacent windows with different glass properties kept distinct?",
        ("multiple_openings", "mixed_glazing", "material_assignment"),
    ),
    SceneSpec(
        "three_room_chain",
        "connections",
        "Can daylight cross two successive internal glass partitions?",
        ("borrowed_light", "serial_glazing", "paired_apertures"),
        3,
    ),
    SceneSpec(
        "glazed_corridor",
        "connections",
        "Does a glazed corridor feed an office and an adjoining meeting room?",
        ("borrowed_light", "turning_light_path", "paired_apertures"),
        3,
    ),
    SceneSpec(
        "stacked_rooms",
        "connections",
        "Does an opaque shared slab isolate two storeys?",
        ("stacked_zones", "opaque_adjacency", "room_isolation"),
        2,
    ),
    SceneSpec(
        "courtyard_rooms",
        "connections",
        "Do four inward-facing rooms shade one another beneath a pergola?",
        ("multiroom_context", "courtyard", "combined_shading"),
        4,
    ),
    SceneSpec(
        "atrium_borrowed_light",
        "connections",
        "Can a rooflit atrium feed rooms at two levels through internal glass?",
        ("roof_glazing", "borrowed_light", "split_adjacency", "stacked_zones"),
        3,
    ),
)
SCENE_SPECS += tuple(
    SceneSpec(
        f"plan_{family}_{profile}",
        "form",
        f"How does a {profile.replace('_', ' ')} opening illuminate a {family.upper()}-shaped plan?",
        ("concave_plan", "reentrant_occlusion", "window_shape", "window_position"),
        footprint_family=family,
        window_profile=profile,
    )
    for family in PLAN_FOOTPRINTS
    for profile in WINDOW_PROFILES
)
SCENE_SPECS += tuple(
    SceneSpec(
        identifier,
        "teaching",
        TEACHING_QUESTIONS[identifier],
        tuple(
            sorted(
                {"side_glazing", "multiple_bounces"}
                | {key for key in TEACHING_SCENES[identifier] if key != "windows"}
            )
        ),
    )
    for identifier in TEACHING_SCENES
)
SCENE_IDS = tuple(spec.identifier for spec in SCENE_SPECS)
_SPECS = {spec.identifier: spec for spec in SCENE_SPECS}
SCENE_CATEGORIES = tuple(dict.fromkeys(spec.category for spec in SCENE_SPECS))


def scene_metadata(identifier):
    """JSON-compatible description retained beside numerical comparison results."""
    try:
        spec = _SPECS[identifier]
    except KeyError:
        raise ValueError("Unknown validation scene: " + identifier) from None
    data = asdict(spec)
    data["interactions"] = list(spec.interactions)
    return {"suite_version": SCENE_VERSION, **data}


def _box(identifier, width=6, depth=6, height=3, origin=(0, 0, 0)):
    from honeybee.room import Room
    from ladybug_geometry.geometry3d import Point3D

    return Room.from_box(identifier, width, depth, height, origin=Point3D(*origin))


def _face(points):
    from ladybug_geometry.geometry3d import Face3D, Point3D

    return Face3D(tuple(Point3D(*point) for point in points))


def _wall(room, direction):
    vector = {
        "south": (0, -1, 0),
        "north": (0, 1, 0),
        "east": (1, 0, 0),
        "west": (-1, 0, 0),
    }[direction]
    return max(
        room.faces, key=lambda face: sum(a * b for a, b in zip(face.normal, vector))
    )


def _window(room, direction="south", width=2, height=1.5, sill=0.8):
    return _wall(room, direction).aperture_by_width_height(width, height, sill)


def _aperture(face, points):
    from honeybee.aperture import Aperture

    geometry = _face(points)
    if geometry.normal.dot(face.normal) < 0:
        geometry = geometry.flip()
    aperture = Aperture(face.identifier + "_opening_%d" % len(face.apertures), geometry)
    face.add_aperture(aperture)
    return aperture


def _rooflight(room, x0=2, y0=2, width=2, depth=2, z=3):
    return _aperture(
        max(room.faces, key=lambda face: face.normal.z),
        (
            (x0, y0, z),
            (x0 + width, y0, z),
            (x0 + width, y0 + depth, z),
            (x0, y0 + depth, z),
        ),
    )


def _shade(parent, name, points, indoor=False):
    from honeybee.shade import Shade

    shade = Shade(parent.identifier + "_" + name, _face(points))
    if indoor:
        parent.add_indoor_shade(shade)
    elif hasattr(parent, "add_outdoor_shade"):
        parent.add_outdoor_shade(shade)
    else:
        parent.add_shade(shade)
    return shade


def _context_box(model, name, width, depth, height, origin):
    for index, face in enumerate(_box(name, width, depth, height, origin).faces):
        _shade(
            model, name + "_%d" % index, tuple(tuple(p) for p in face.geometry.boundary)
        )


def _footprint(identifier, points):
    from honeybee.room import Room
    from ladybug_geometry.geometry3d import Polyface3D

    return Room.from_polyface3d(
        identifier,
        Polyface3D.from_offset_face(_face(tuple((x, y, 0) for x, y in points)), 3),
    )


def _connect(first, second, direction, width=2, height=1.5, sill=0.8):
    opposite = {"east": "west", "west": "east", "north": "south", "south": "north"}[
        direction
    ]
    _window(first, direction, width, height, sill)
    _window(second, opposite, width, height, sill)


def _edge_wall(room, start, end):
    """Select the unique wall on a boundary segment, not a cardinal direction."""
    x, y = ((a + b) / 2 for a, b in zip(start, end))
    matches = [
        face
        for face in room.faces
        if abs(face.normal.z) < 1e-8
        and abs(face.center.x - x) < 1e-8
        and abs(face.center.y - y) < 1e-8
    ]
    if len(matches) != 1:
        raise ValueError("Footprint edge does not identify a unique wall")
    return matches[0]


def _plan_room(identifier):
    import math

    spec = _SPECS[identifier]
    points = PLAN_FOOTPRINTS[spec.footprint_family]
    room = _footprint(identifier, points)
    edges = list(zip(points, (*points[1:], points[0])))
    if spec.window_profile != "distributed":
        # CCW east-going edges face south; choose the lowest, then leftmost.
        edges = [
            min(
                (
                    edge
                    for edge in edges
                    if edge[1][0] > edge[0][0] and edge[1][1] == edge[0][1]
                ),
                key=lambda edge: (edge[0][1], edge[0][0]),
            )
        ]
    for start, end in edges:
        length = math.dist(start, end)
        center = length / 2
        profile = spec.window_profile
        if profile in (
            "small_center",
            "large_center",
            "offset_low",
            "offset_high",
            "distributed",
        ):
            width, height, sill = 1.2, 1.2, 0.9
            if profile == "large_center":
                width, height, sill = 2.4, 2, 0.5
            elif profile == "offset_low":
                center, sill = 0.8, 0.2
            elif profile == "offset_high":
                center, sill = length - 0.8, 1.6
            elif profile == "distributed":
                width, sill = 1, 0.8
            local = (
                (center - width / 2, sill),
                (center + width / 2, sill),
                (center + width / 2, sill + height),
                (center - width / 2, sill + height),
            )
        elif profile == "triangle":
            local = ((center - 1, 0.78), (center + 1, 0.78), (center, 2.22))
        elif profile == "circle":
            radius = math.sqrt(1.44 / (16 * math.sin(math.pi / 16)))
            local = tuple(
                (
                    center + radius * math.cos(2 * math.pi * i / 32),
                    1.5 + radius * math.sin(2 * math.pi * i / 32),
                )
                for i in range(32)
            )
        else:  # Polygonal arch: rectangular portion plus 16-segment semicircle.
            radius = 0.6
            rectangle_height = (1.44 - 8 * radius**2 * math.sin(math.pi / 16)) / 1.2
            bottom = 1.5 - (rectangle_height + radius) / 2
            spring = bottom + rectangle_height
            local = (
                (center - radius, bottom),
                (center + radius, bottom),
                *tuple(
                    (
                        center + radius * math.cos(math.pi * i / 16),
                        spring + radius * math.sin(math.pi * i / 16),
                    )
                    for i in range(17)
                ),
            )
        dx, dy = ((b - a) / length for a, b in zip(start, end))
        _aperture(
            _edge_wall(room, start, end),
            tuple((start[0] + dx * s, start[1] + dy * s, z) for s, z in local),
        )
    return room


def _pitched_room(identifier):
    from honeybee.room import Room
    from ladybug_geometry.geometry3d import Polyface3D

    points = (
        (0, 0, 0),
        (6, 0, 0),
        (6, 8, 0),
        (0, 8, 0),
        (0, 0, 3),
        (6, 0, 3),
        (6, 8, 3),
        (0, 8, 3),
        (3, 0, 4.5),
        (3, 8, 4.5),
    )
    # Floor, two gables, two walls, and two planar roof slopes.
    indices = (
        (0, 3, 2, 1),
        (0, 1, 5, 8, 4),
        (3, 7, 9, 6, 2),
        (0, 4, 7, 3),
        (1, 2, 6, 5),
        (4, 8, 9, 7),
        (8, 5, 6, 9),
    )
    faces = tuple(_face(tuple(points[i] for i in face)) for face in indices)
    return Room.from_polyface3d(identifier, Polyface3D.from_faces(faces, 0.01))


def _atrium_rooms(identifier):
    from honeybee.face import Face
    from honeybee.room import Room

    atrium = _box(identifier + "_atrium", height=6)
    east = _wall(atrium, "east")
    faces = [face for face in atrium.faces if face is not east]
    for level in range(2):
        z0, z1 = level * 3, (level + 1) * 3
        faces.append(
            Face(
                identifier + "_atrium_east_%d" % level,
                _face(((6, 0, z0), (6, 6, z0), (6, 6, z1), (6, 0, z1))),
            )
        )
    atrium = Room(atrium.identifier, faces)
    offices = [
        _box(identifier + "_office_%d" % level, origin=(6, 0, level * 3))
        for level in range(2)
    ]
    _rooflight(atrium, 1, 1, 4, 4, z=6)
    for level, office in enumerate(offices):
        faces[-2 + level].aperture_by_width_height(3, 1.6, 0.8)
        _window(office, "west", 3, 1.6, 0.8)
    return [atrium, *offices]


def _rooms(identifier):
    """Construct form and openings before finishes, shades and sensor grids."""
    if _SPECS[identifier].footprint_family:
        return [_plan_room(identifier)]
    if identifier in TEACHING_SCENES:
        parameters = teaching_parameters(identifier)
        room = _box(identifier, *parameters["room"])
        width, height, sill = parameters["window"]
        count = parameters.get("windows", 1)
        wall_width = parameters["room"][0]
        pitch = wall_width / count
        for index in range(count):
            center = pitch * (index + 0.5)
            _aperture(
                _wall(room, "south"),
                (
                    (center - width / 2, 0, sill),
                    (center + width / 2, 0, sill),
                    (center + width / 2, 0, sill + height),
                    (center - width / 2, 0, sill + height),
                ),
            )
        return [room]
    if identifier == "three_room_chain":
        rooms = [
            _box(identifier + "_%d" % i, depth=4, origin=(0, i * 4, 0))
            for i in range(3)
        ]
        _window(rooms[0])
        for first, second in zip(rooms, rooms[1:]):
            _connect(first, second, "north")
        return rooms
    if identifier == "glazed_corridor":
        rooms = [
            _box(identifier + "_corridor", depth=3),
            _box(identifier + "_office", origin=(0, 3, 0)),
            _box(identifier + "_meeting", origin=(6, 3, 0)),
        ]
        _window(rooms[0], width=4, height=1.8, sill=0.6)
        _connect(rooms[0], rooms[1], "north", width=2.5)
        _connect(rooms[1], rooms[2], "east")
        return rooms
    if identifier == "stacked_rooms":
        rooms = [_box(identifier + "_%d" % i, origin=(0, 0, i * 3)) for i in range(2)]
        for room in rooms:
            _window(room)
        return rooms
    if identifier == "courtyard_rooms":
        rooms = [
            _box(identifier + "_west", 4, 8),
            _box(identifier + "_east", 4, 8, origin=(10, 0, 0)),
            _box(identifier + "_north", 6, 4, origin=(4, 8, 0)),
            _box(identifier + "_south", 6, 4, origin=(4, -4, 0)),
        ]
        for room, direction in zip(rooms, ("east", "west", "south", "north")):
            _window(room, direction, width=3)
        return rooms
    if identifier == "atrium_borrowed_light":
        return _atrium_rooms(identifier)
    dimensions = {
        "shallow_plan": (8, 3, 3),
        "narrow_corridor": (3, 15, 3),
        "double_height": (6, 6, 6),
    }
    if identifier == "pitched_roof":
        room = _pitched_room(identifier)
    elif identifier in ("trapezoid_plan", "u_shaped_plan"):
        plans = {
            "trapezoid_plan": ((0, 0), (6, 0), (8, 7), (-2, 7)),
            "u_shaped_plan": (
                (0, 0),
                (9, 0),
                (9, 9),
                (6, 9),
                (6, 3),
                (3, 3),
                (3, 9),
                (0, 9),
            ),
        }
        room = _footprint(identifier, plans[identifier])
    else:
        room = _box(identifier, *dimensions.get(identifier, (6, 6, 3)))
    if identifier == "multiple_rooflights":
        for x in (1, 4):
            for y in (1, 4):
                _rooflight(room, x, y, 1, 1)
    elif identifier == "rooflight_well":
        _rooflight(room)
    elif identifier in ("ribbon_windows", "mixed_glazing"):
        for center in (1, 3, 5) if identifier == "ribbon_windows" else (1.5, 4.5):
            width = 1.4 if identifier == "ribbon_windows" else 1.6
            _aperture(
                _wall(room, "south"),
                (
                    (center - width / 2, 0, 0.8),
                    (center + width / 2, 0, 0.8),
                    (center + width / 2, 0, 2.3),
                    (center - width / 2, 0, 2.3),
                ),
            )
    elif identifier in ("north_facing", "east_facing", "west_facing"):
        _window(room, identifier.split("_")[0])
    elif identifier == "clerestory":
        _window(room, width=4, height=0.5, sill=2.3)
    elif identifier == "full_height_glazing":
        _window(room, width=5.6, height=2.7, sill=0.15)
    elif identifier == "double_height":
        _window(room, width=4, height=4.5, sill=0.5)
    else:
        _window(room, width=1.5 if identifier == "narrow_corridor" else 2)
        if identifier == "corner_glazing":
            _window(room, "east")
        elif identifier == "opposite_glazing":
            _window(room, "north")
        elif identifier == "u_shaped_plan":
            _window(room, "east")
            _window(room, "west")
    return [room]


def _shading(model, identifier):
    room = model.rooms[0]
    aperture = room.apertures[0] if room.apertures else None
    if identifier in TEACHING_SCENES and teaching_parameters(identifier)["overhang"]:
        aperture.overhang(teaching_parameters(identifier)["overhang"])
    if identifier in ("deep_overhang", "rotated_37"):
        aperture.overhang(2 if identifier == "deep_overhang" else 0.9)
    if identifier in ("asymmetric_fins", "rotated_37"):
        for index, (x, depth) in enumerate(
            ((2, 0.4), (4, 1.5))
            if identifier == "asymmetric_fins"
            else ((2, 1), (4, 1))
        ):
            _shade(
                aperture,
                "fin_%d" % index,
                ((x, 0, 0.8), (x, -depth, 0.8), (x, -depth, 2.3), (x, 0, 2.3)),
            )
    if identifier in ("horizontal_louvres", "eggcrate"):
        for index, z in enumerate((0.95, 1.35, 1.75, 2.15)):
            _shade(
                aperture,
                "horizontal_%d" % index,
                (
                    (1.8, -0.9, z + 0.12),
                    (4.2, -0.9, z + 0.12),
                    (4.2, -0.05, z),
                    (1.8, -0.05, z),
                ),
            )
    if identifier in ("vertical_louvres", "eggcrate"):
        for index, x in enumerate((2, 2.5, 3, 3.5, 4)):
            _shade(
                aperture,
                "vertical_%d" % index,
                ((x, -0.9, 0.65), (x, -0.05, 0.65), (x, -0.05, 2.5), (x, -0.9, 2.5)),
            )
    if identifier == "light_shelf":
        _shade(
            aperture,
            "outer_shelf",
            ((1.8, -0.7, 1.65), (4.2, -0.7, 1.65), (4.2, 0, 1.65), (1.8, 0, 1.65)),
        )
        _shade(
            room,
            "inner_shelf",
            ((1.8, 0, 1.65), (4.2, 0, 1.65), (4.2, 1.5, 1.65), (1.8, 1.5, 1.65)),
            indoor=True,
        )
    if identifier == "recessed_window":
        for name, points in (
            ("left", ((2, 0, 0.8), (2, -0.6, 0.8), (2, -0.6, 2.3), (2, 0, 2.3))),
            ("right", ((4, 0, 0.8), (4, -0.6, 0.8), (4, -0.6, 2.3), (4, 0, 2.3))),
            ("top", ((2, 0, 2.3), (4, 0, 2.3), (4, -0.6, 2.3), (2, -0.6, 2.3))),
            ("sill", ((2, 0, 0.8), (4, 0, 0.8), (4, -0.6, 0.8), (2, -0.6, 0.8))),
        ):
            _shade(aperture, "reveal_" + name, points)
    if identifier == "rooflight_well":
        for index, (first, second) in enumerate(
            (((2, 2), (4, 2)), ((4, 2), (4, 4)), ((4, 4), (2, 4)), ((2, 4), (2, 2)))
        ):
            x0, y0 = first
            x1, y1 = second
            _shade(
                room,
                "well_%d" % index,
                ((x0, y0, 2), (x1, y1, 2), (x1, y1, 3), (x0, y0, 3)),
                indoor=True,
            )
    if identifier == "balcony_above":
        _context_box(model, "balcony", 6.4, 2.1, 0.2, (-0.2, -2, 3.05))
    if identifier == "courtyard_rooms":
        for index, y in enumerate((0.5, 2.5, 4.5, 6.5)):
            _shade(
                model,
                "pergola_%d" % index,
                ((4, y, 3.5), (10, y, 3.5), (10, y + 0.4, 3.5), (4, y + 0.4, 3.5)),
            )


def _context(model, identifier):
    if identifier in TEACHING_SCENES and teaching_parameters(identifier)["obstruction"]:
        # Obstruction angle measured from the window centre to the top of a
        # facade 10 m away across the street, as in BRE/BS 8206 site layout.
        import math

        angle = teaching_parameters(identifier)["obstruction"]
        _, height, sill = teaching_parameters(identifier)["window"]
        top = sill + height / 2 + 10 * math.tan(math.radians(angle))
        _context_box(model, "street_facade", 40, 2, top, (-17, -12, 0))
    if identifier == "reflective_neighbour":
        _shade(model, "neighbour", ((-2, -2, 0), (8, -2, 0), (8, -2, 5), (-2, -2, 5)))
    elif identifier == "urban_canyon":
        for name, y in (("south_block", -6), ("north_block", 8)):
            _context_box(model, name, 18, 2, 12, (-6, y, 0))
    elif identifier == "courtyard_context":
        _context_box(model, "west_block", 2, 14, 7, (-3, -5, 0))
        _context_box(model, "east_block", 2, 14, 7, (7, -5, 0))
        _context_box(model, "south_block", 8, 2, 7, (-1, -7, 0))
    elif identifier == "offset_tower":
        _context_box(model, "tower", 4, 5, 18, (7, -4, 0))


def _finishes(model, identifier):
    from honeybee_radiance.modifier.material import Plastic, Glass

    reflectance = 0.1 if identifier == "dark_interior" else 0.5
    if identifier in TEACHING_SCENES:
        reflectance = teaching_parameters(identifier)["reflectance"]
    opaque = Plastic.from_single_reflectance("diffuse", reflectance)
    glass = Glass.from_single_transmittance(
        "clear", 0.2 if identifier == "low_transmittance" else 0.6
    )
    for face in model.faces:
        face.properties.radiance.modifier = opaque
        if (
            identifier == "bright_ceiling"
            and face.type.__class__.__name__ == "RoofCeiling"
        ):
            face.properties.radiance.modifier = Plastic.from_single_reflectance(
                "bright_ceiling", 0.9
            )
        elif identifier == "coloured_walls" and face.type.__class__.__name__ == "Wall":
            face.properties.radiance.modifier = Plastic("red_walls", 0.7, 0.15, 0.1)
    for aperture in model.apertures:
        aperture.properties.radiance.modifier = glass
    if identifier == "mixed_glazing":
        for aperture, transmittance in zip(model.apertures, (0.25, 0.8)):
            aperture.properties.radiance.modifier = Glass.from_single_transmittance(
                "glass_%s" % transmittance, transmittance
            )
    shade_reflectance = (
        0.85 if identifier in ("reflective_neighbour", "light_shelf") else 0.2
    )
    for shade in model.shades:
        shade.properties.radiance.modifier = Plastic.from_single_reflectance(
            "shade_diffuse", shade_reflectance
        )


def make_scene(identifier, repository=None):
    """Build an independent Honeybee model with finishes and explicit workplanes."""
    from honeybee.model import Model
    from honeybee.room import Room
    from honeybee_radiance.sensorgrid import SensorGrid

    metadata = scene_metadata(identifier)
    repository = Path(repository) if repository else Path(__file__).resolve().parents[1]
    if identifier in _LEGACY_IDS:
        model = _legacy_scene(identifier, repository)
    else:
        rooms = _rooms(identifier)
        Room.solve_adjacency(rooms)
        model = Model(identifier, rooms, units="Meters", tolerance=0.01)
        _shading(model, identifier)
        _context(model, identifier)
        _finishes(model, identifier)
        for room in rooms:
            mesh = room.generate_grid(1, offset=0.75)
            if mesh is None or not mesh.faces:
                raise ValueError("Scene has no usable workplane: " + room.identifier)
            grid = SensorGrid.from_mesh3d(room.identifier + "_grid", mesh)
            grid.room_identifier = room.identifier
            model.properties.radiance.add_sensor_grid(grid)
        if identifier == "rotated_37":
            from ladybug_geometry.geometry3d import Point3D

            model.rotate_xy(37, Point3D(3, 3, 0))
    model.user_data = {**(model.user_data or {}), "validation_scene": metadata}
    # Honeybee normalizes face planes/vertex order on HBJSON load. Use that same
    # representation in memory so exports preserve fingerprints and mesh arrays.
    return Model.from_dict(model.to_dict())


def scene_dict(model):
    """Stable daylight HBJSON: sort unordered libraries, preserve geometry/grids."""

    def canonical(value):
        if isinstance(value, dict):
            result = {key: canonical(item) for key, item in value.items()}
            for key in ("modifiers", "modifier_sets"):
                if key in result:
                    result[key] = sorted(
                        result[key], key=lambda item: item["identifier"]
                    )
            return result
        if isinstance(value, (list, tuple)):
            return [canonical(item) for item in value]
        return value

    # Optional Energy plugins must not change daylight sample files.
    return canonical(model.to_dict(included_prop=["radiance"]))


def export_scenes(output, identifiers=SCENE_IDS, repository=None):
    """Export validated HBJSON samples and a coverage manifest to a new directory."""
    import hashlib
    import json

    identifiers = tuple(identifiers)
    if not identifiers or len(set(identifiers)) != len(identifiers):
        raise ValueError("Choose at least one scene, without duplicates")
    for identifier in identifiers:
        scene_metadata(identifier)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    records = []
    for identifier in identifiers:
        model = make_scene(identifier, repository)
        errors = model.check_all(raise_exception=False, detailed=True)
        if errors:
            raise ValueError("Invalid scene %s: %s" % (identifier, errors))
        path = output / (identifier + ".hbjson")
        payload = json.dumps(scene_dict(model), sort_keys=True, indent=2) + "\n"
        path.write_text(payload, encoding="utf-8")
        records.append(
            {
                **scene_metadata(identifier),
                "file": path.name,
                "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
                "rooms": len(model.rooms),
                "apertures": len(model.apertures),
                "shades": len(model.shades),
                "sensors": sum(
                    grid.count for grid in model.properties.radiance.sensor_grids
                ),
            }
        )
    manifest = {
        "suite_version": SCENE_VERSION,
        "scene_count": len(records),
        "units": "Meters",
        "scenes": records,
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    lines = [
        "# Architectural daylight sample models",
        "",
        "Generated fixtures; numerical acceptance requires the Radiance comparison suite.",
        "",
        "| Scene | Category | Architectural question |",
        "| --- | --- | --- |",
    ]
    lines.extend(
        "| [%s](%s) | %s | %s |"
        % (record["identifier"], record["file"], record["category"], record["question"])
        for record in records
    )
    (output / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return manifest


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--scene", choices=SCENE_IDS, action="append")
    parser.add_argument("--category", choices=SCENE_CATEGORIES, action="append")
    parser.add_argument(
        "--list",
        action="store_true",
        help="List architectural questions without installing Honeybee",
    )
    args = parser.parse_args(argv)
    identifiers = tuple(
        spec.identifier
        for spec in SCENE_SPECS
        if (not args.scene or spec.identifier in args.scene)
        and (not args.category or spec.category in args.category)
    )
    if not identifiers:
        parser.error("No scenes match the selected scenes and categories")
    if args.list:
        for identifier in identifiers:
            metadata = scene_metadata(identifier)
            print(
                "%s [%s]: %s" % (identifier, metadata["category"], metadata["question"])
            )
    else:
        if args.output is None:
            parser.error("--output is required when exporting models")
        manifest = export_scenes(args.output, identifiers)
        print(
            "Exported %d architectural scenes to %s"
            % (manifest["scene_count"], args.output)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
