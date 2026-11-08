"""Demo building for "Foton Interactive Demo.gh": rooms in a row, floors stacked.

Builds a Honeybee Model from the demo's sliders: one or more floors, each a
row of identical rooms side by side along the width, with a sensor grid at desk
height in every room. Outside walls get windows at the ratios set per facade,
with an overhang over each window. If asked for, a neighbouring block faces the
south wall. Everything is rotated together, so rotation turns the whole site:
at 0 degrees the "south" wall faces south.

Inputs: width, depth, height (of each room), floors, rooms, rotation,
wwr_south, wwr_east, wwr_north, wwr_west, overhang, neighbour, distance
Outputs: model, grid_mesh, df_mesh (one mesh per room), walls, glass, shades,
context
"""
import glob
import os
import sys


def find_ladybug_tools():
    """Rhino 8's script component does not search Ladybug Tools' folder by itself."""
    try:
        import ladybug_rhino  # noqa: F401
        return
    except ImportError:
        pass
    home = os.path.expanduser("~")
    patterns = (
        os.path.join(home, "ladybug_tools", "python", "lib", "python3*", "site-packages"),
        os.path.join(home, "ladybug_tools", "python", "Lib", "site-packages"),
    )
    for pattern in patterns:
        for folder in sorted(glob.glob(pattern)):
            if folder not in sys.path:
                sys.path.append(folder)
    try:
        import ladybug_rhino  # noqa: F401
    except ImportError:
        raise ImportError("This demo needs Ladybug Tools: install it from food4rhino.com")


find_ladybug_tools()

from ladybug_geometry.geometry3d import Point3D, Vector3D, Polyface3D
from honeybee.room import Room
from honeybee.shade import Shade
from honeybee.model import Model
from ladybug_rhino.fromgeometry import from_face3d, from_mesh3d

GRID_SIZE = 0.5
GRID_HEIGHT = 0.75
NEIGHBOUR_HEIGHT = 12.0
NEIGHBOUR_DEPTH = 6.0


def number(value, default, low, high):
    # An unconnected input is None, and float(None) is a .NET error in IronPython.
    value = default if value is None else float(value)
    return min(max(value, low), high)


width = number(width, 6.0, 2.0, 20.0)
depth = number(depth, 10.0, 2.0, 20.0)
height = number(height, 3.0, 2.2, 6.0)
angle = number(rotation, 0.0, -360.0, 360.0)
ratios = {
    "south": number(wwr_south, 0.3, 0.0, 0.95),
    "east": number(wwr_east, 0.0, 0.0, 0.95),
    "north": number(wwr_north, 0.0, 0.0, 0.95),
    "west": number(wwr_west, 0.0, 0.0, 0.95),
}
overhang_depth = number(overhang, 0.0, 0.0, 3.0)
gap = number(distance, 10.0, 2.0, 50.0)

floor_count = int(number(floors, 1, 1, 6))
room_count = int(number(rooms, 1, 1, 6))
total_width = width * room_count

rooms_ = []
for level in range(floor_count):
    for index in range(room_count):
        rooms_.append(Room.from_box(
            "DemoRoom_F%d_R%d" % (level + 1, index + 1), width, depth, height,
            origin=Point3D(index * width, 0, level * height)))
if len(rooms_) > 1:
    # Shared walls and floors become interior, so only outside walls get windows.
    Room.solve_adjacency(rooms_, 0.01)

directions = {"south": (0, -1), "east": (1, 0), "north": (0, 1), "west": (-1, 0)}
for room in rooms_:
    for face in room.faces:
        if face.type.name != "Wall" or face.boundary_condition.name != "Outdoors":
            continue
        normal = face.normal
        for side, (x, y) in directions.items():
            if normal.x * x + normal.y * y > 0.9 and ratios[side] > 0.01:
                # Windows start 0.8 m above the floor, like a desk-height sill.
                face.apertures_by_ratio_rectangle(
                    ratios[side], aperture_height=height - 0.8 - 0.3,
                    sill_height=0.8, horizontal_separation=3.0, tolerance=0.01)
                if overhang_depth > 0.01:
                    for aperture in face.apertures:
                        aperture.overhang(overhang_depth, indoor=False, tolerance=0.01)

shades = []
if neighbour:
    # A block three times as wide as the building, facing the south wall across a street.
    x0, x1 = -total_width, 2.0 * total_width
    y1 = -gap
    y0 = y1 - NEIGHBOUR_DEPTH
    block_height = max(NEIGHBOUR_HEIGHT, floor_count * height)
    block = Polyface3D.from_box(x1 - x0, NEIGHBOUR_DEPTH, block_height, base_plane=None)
    block = block.move(Vector3D(x0, y0, 0))
    shades = [Shade("Neighbour_%d" % index, face) for index, face in enumerate(block.faces)]

grids = [room.properties.radiance.generate_sensor_grid(GRID_SIZE, offset=GRID_HEIGHT)
         for room in rooms_]
model = Model("FotonDemo", rooms=rooms_, orphaned_shades=shades, units="Meters",
              tolerance=0.01, angle_tolerance=1.0)
model.properties.radiance.add_sensor_grids(grids)
if abs(angle) > 1e-6:
    # Honeybee turns counterclockwise; the slider turns clockwise like a compass.
    model.rotate_xy(-angle, Point3D(total_width / 2.0, depth / 2.0, 0))

grids = model.properties.radiance.sensor_grids
grid_mesh = [from_mesh3d(grid.mesh) for grid in grids]
# The daylight factor plans sit beside the building so both heatmaps can be seen.
offset = Vector3D(max(total_width, depth) + 3.0, 0, -GRID_HEIGHT)
df_mesh = [from_mesh3d(grid.mesh.move(offset)) for grid in grids]
outside = [face for room in model.rooms for face in room.faces
           if face.type.name == "Wall" and face.boundary_condition.name == "Outdoors"]
walls = [from_face3d(face.punched_geometry) for face in outside]
glass = [from_face3d(aperture.geometry) for face in outside for aperture in face.apertures]
shades = [from_face3d(shade.geometry) for face in outside for aperture in face.apertures
          for shade in aperture.outdoor_shades]
context = [from_face3d(shade.geometry) for shade in model.orphaned_shades]
