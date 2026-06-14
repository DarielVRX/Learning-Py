import json
import random

x = 0
y = 0

size = 20
surface = [13, 14, 15, 16]
world = '0003'
AIR = 'air'
GRASS = 'grass'
DIRT = 'dirt'
ROCK = 'rock'
material = [GRASS, DIRT, ROCK, AIR]
block = {}
random.seed(f"{world}")

for i in range(size):
    x = i
    for j in range (size - 1, -1, -1):
        y = j
        pos = [x, y]
        p_id = f"{x}_{y}"

        if y == size - 1:
            _material = AIR

        elif size - 1 > y > max(surface):
            if block[f"{x}_{y+1}"]["material"] == AIR:
                _material = random.choices(material, weights=[70, 4, 1, 25])[0]
            elif block[f"{x}_{y+1}"]["material"] in (GRASS, DIRT):
                _material = DIRT
            else:
                _material = ROCK

        elif y in surface:
            if block[f"{x}_{y+1}"]["material"] == AIR:
                _material = random.choices(material, weights=[60, 25, 15, 0])[0]
            elif block[f"{x}_{y+1}"]["material"] in (GRASS, DIRT):
                _material = random.choices(material, weights=[0, 60, 40, 0])[0]
            else:
                _material = ROCK

        else:
            _material = ROCK

        block[f"{p_id}"] = {
            "material": _material
        }

tiles = {
    "air": "   ",
    "grass": " | ",
    "dirt": " x ",
    "rock": " o "
    }

for y in range(size - 1, -1, -1):
    for x in range(size):
        print(tiles[block[f"{x}_{y}"]["material"]], end="")
    print()


with open("draft.json", "w") as f:
    json.dump(block, f, indent=4)
