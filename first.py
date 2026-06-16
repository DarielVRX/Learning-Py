import json
import random

AIR = 'air'
GRASS = 'grass'
DIRT = 'dirt'
ROCK = 'rock'
GOLD = 'gold'
tiles = {
    "air": " ",
    "grass": "=",
    "dirt": "x",
    "rock": "#",
    "gold": "0"
    }
material = [GRASS, DIRT, ROCK, AIR, GOLD]
block = {}
neighborhood = []

world = '0003'
random.seed(f"{world}")

size = 30
chunks = 10
sur_min = 16
sur_max = 22
surface = []
x = 0
y = 0

for i in range(sur_min, sur_max + 1):
    surface.append(i)

def gen_chunk():
    global x
    for x in range(x + size):
        for y in range (size - 1, -1, -1):
            pos = [x, y]
            p_id = f"{x}_{y}"

            if y == size - 1:
                _material = AIR

            elif size - 1 > y > max(surface):
                if block[f"{x}_{y+1}"]["material"] == AIR:
                    _material = random.choices(material, weights=[60, 4, 1, 35, 0])[0]
                elif block[f"{x}_{y+1}"]["material"] in (GRASS, DIRT):
                    _material = DIRT
                else:
                    _material = ROCK

            elif y in surface:
                if block[f"{x}_{y+1}"]["material"] == AIR:
                    _material = random.choices(material, weights=[60, 25, 15, 0, 0])[0]
                elif block[f"{x}_{y+1}"]["material"] in (GRASS, DIRT):
                    _material = random.choices(material, weights=[0, 60, 40, 0, 0])[0]
                else:
                    _material = ROCK

            else:
                if GOLD in neighborhood:
                    _material = random.choices(material, weights=[0, 0, 90, 0, 10])[0]
                else:
                    _material = random.choices(material, weights=[0, 0, 95, 0, 5])[0]

            block[f"{p_id}"] = {
                "material": _material
            }

            neighborhood = []

            for i in range(-1, 2):
                for j in range(-2, 1):
                    if (y + j) >= 0 and (y + j) <= size - 1:
                        if (x + i) >= 0 and (x + i) <= x - 1:
                            neighborhood.append(block[f"{x + i}_{y + j}"]["material"])
                        elif (x + i) >= 0 and (y + j) >= y and (x + i) <= x:
                            neighborhood.append(block[f"{x + i}_{y + j}"]["material"])

for i in range(chunks):
        gen_chunk()

for x in range((size - 1) * chunks):
    for y in range(size):
            print(tiles[block[f"{x}_{y}"]["material"]], end="")

    print()

with open("draft.json", "w") as f:
    json.dump(block, f, indent=4)
