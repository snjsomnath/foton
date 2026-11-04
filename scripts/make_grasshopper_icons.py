#!/usr/bin/env python3
"""Draw the 24x24 Grasshopper icons for the Foton components and the Yak package icon.

Run once after changing a design; build_grasshopper.py embeds the PNGs in the
user objects. Each icon is drawn at 8x and scaled down so edges stay smooth.
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "grasshopper_foton" / "icons"
SIZE, SCALE = 24, 8
S = SIZE * SCALE

INK = (31, 58, 95, 255)        # deep blue outline
SUN = (245, 166, 35, 255)      # amber
CLOUD = (176, 186, 199, 255)
# Low to high illuminance, like a Ladybug heatmap.
HEAT = [(50, 74, 160, 255), (64, 160, 190, 255), (120, 196, 110, 255), (245, 210, 60, 255), (240, 120, 40, 255)]


def px(value):
    return value * SCALE


def canvas():
    image = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    return image, ImageDraw.Draw(image)


def sun(draw, cx, cy, radius, rays=8, ray_length=3.2, width=1.4):
    for index in range(rays):
        angle = 2 * math.pi * index / rays
        inner = radius + 1.2
        outer = inner + ray_length
        draw.line(
            [px(cx + inner * math.cos(angle)), px(cy + inner * math.sin(angle)),
             px(cx + outer * math.cos(angle)), px(cy + outer * math.sin(angle))],
            fill=SUN, width=int(px(width)),
        )
    draw.ellipse([px(cx - radius), px(cy - radius), px(cx + radius), px(cy + radius)], fill=SUN, outline=INK, width=int(px(0.9)))


def heat_grid(draw, x, y, cell, pattern):
    rows, columns = len(pattern), len(pattern[0])
    for row in range(rows):
        for column in range(columns):
            colour = HEAT[pattern[row][column]]
            box = [px(x + column * cell), px(y + row * cell), px(x + (column + 1) * cell), px(y + (row + 1) * cell)]
            draw.rectangle(box, fill=colour)
    draw.rectangle([px(x), px(y), px(x + columns * cell), px(y + rows * cell)], outline=INK, width=int(px(1)))


def cloud(draw, x, y):
    puffs = ((x + 4, y + 5.2, 3.2), (x + 8.5, y + 3.8, 4.2), (x + 13, y + 5.6, 3.0))
    edge = 1.0
    # Outline first (each puff a little larger), then the fill on top, so the
    # overlaps leave no inner lines.
    for colour, grow in ((INK, edge), (CLOUD, 0)):
        for cx, cy, r in puffs:
            r += grow
            draw.ellipse([px(cx - r), px(cy - r), px(cx + r), px(cy + r)], fill=colour)
        draw.rectangle([px(x + 4), px(y + 5), px(x + 13), px(y + 8.6 + grow)], fill=colour)


def settings():
    image, draw = canvas()
    cx = cy = 12
    teeth = 8
    for index in range(teeth):
        angle = 2 * math.pi * index / teeth
        draw.line([px(cx), px(cy), px(cx + 10 * math.cos(angle)), px(cy + 10 * math.sin(angle))], fill=INK, width=int(px(3.6)))
    draw.ellipse([px(cx - 8), px(cy - 8), px(cx + 8), px(cy + 8)], fill=INK)
    draw.ellipse([px(cx - 5), px(cy - 5), px(cx + 5), px(cy + 5)], fill=(255, 255, 255, 255))
    draw.ellipse([px(cx - 3.6), px(cy - 3.6), px(cx + 3.6), px(cy + 3.6)], fill=SUN)
    return image


def annual():
    image, draw = canvas()
    heat_grid(draw, 8.5, 9.5, 4.6, [[1, 2, 3], [0, 2, 4], [0, 1, 3]])
    sun(draw, 6.5, 6.5, 3.6, ray_length=2.4)
    return image


def daylight_factor():
    image, draw = canvas()
    heat_grid(draw, 1.5, 13.5, 4.3, [[3, 2, 1], [2, 1, 0]])
    cloud(draw, 3.5, 2)
    # "%" sign under the cloud
    draw.ellipse([px(15.5), px(14), px(18.5), px(17)], outline=INK, width=int(px(1.1)))
    draw.ellipse([px(19.5), px(19.5), px(22.5), px(22.5)], outline=INK, width=int(px(1.1)))
    draw.line([px(22.5), px(14), px(15.5), px(22.5)], fill=INK, width=int(px(1.3)))
    return image


def results():
    image, draw = canvas()
    # A results folder with a heatmap sheet coming out of it.
    draw.rounded_rectangle([px(1.5), px(8.5), px(22.5), px(22.5)], radius=px(1.5), fill=(214, 225, 238, 255), outline=INK, width=int(px(1)))
    draw.rounded_rectangle([px(1.5), px(6), px(10), px(10)], radius=px(1), fill=(214, 225, 238, 255), outline=INK, width=int(px(1)))
    draw.rectangle([px(2.5), px(8.5), px(9.5), px(10.5)], fill=(214, 225, 238, 255))
    heat_grid(draw, 7, 1.5, 4.2, [[3, 4, 2], [2, 3, 1], [1, 1, 0]])
    return image


ICONS = {
    "Foton Settings": settings,
    "Foton Annual Daylight": annual,
    "Foton Daylight Factor": daylight_factor,
    "Foton Annual Results": results,
}


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, draw in ICONS.items():
        image = draw().resize((SIZE, SIZE), Image.LANCZOS)
        image.save(OUTPUT / (name + ".png"), optimize=True)
        image.resize((SIZE * 8, SIZE * 8), Image.NEAREST).save(Path(__import__("tempfile").gettempdir()) / (name + "-preview.png"))
        print(OUTPUT / (name + ".png"))
    # The package icon in Rhino's Package Manager: the annual design, larger.
    package = annual().resize((128, 128), Image.LANCZOS)
    package.save(ROOT / "grasshopper_foton" / "yak" / "icon.png", optimize=True)
    print(ROOT / "grasshopper_foton" / "yak" / "icon.png")


if __name__ == "__main__":
    main()
