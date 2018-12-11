from day6_input import inp as inp
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

coordinates = []
min_x = 1000
max_x = 0
min_y = 1000
max_y = 0

cntr = -1

for a in inp.split('\n'):
    cntr += 1
    _x, _y = a.split(',')
    _x = int(_x)
    _y = int(_y)
    coordinates.append((cntr, (_x, _y)))

    if _x < min_x:
        min_x = _x
    if _x > max_x:
        max_x = _x
    if _y < min_y:
        min_y = _y
    if _y > max_y:
        max_y = _y

grid = {}

for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        grid[(x, y)] = {}

        for coord_id, coords in coordinates:
            cx, cy = coords
            try:
                grid[(x, y)][abs((cx - x)) + abs((cy - y))].append(coord_id)
            except:
                grid[(x, y)][abs((cx - x)) + abs((cy - y))] = [coord_id]
        # print (x, y), min(grid[(x, y)].keys()), grid[(x, y)][min(grid[(x, y)].keys())], grid[(x, y)]


ids = [0] * 50
for coord, deets in grid.items():
    if len(deets[min(deets.keys())]) == 1:
        ids[deets[min(deets.keys())][0]] += 1

print max(ids)

# plt.scatter(*zip(*coordinates))
# plt.grid(True)
# plt.show()


# PART 2

region_size = 10000
in_region = 0
for x in range(0, region_size):
    for y in range(0, region_size):
        total_distance = 0


        for coord_id, coords in coordinates:
            cx, cy = coords
            distance = abs((cx - x)) + abs((cy - y))
            total_distance += distance

            # print coords, distance, total_distance

        if total_distance < region_size:
            print (x, y)
            in_region += 1

print in_region



