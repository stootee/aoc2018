from inputs.day10 import input as inp
import matplotlib.pyplot as plt

def parse(_inp):
    _inp = _inp.replace("position=", "").replace(" velocity", "").replace("<", "").replace(">", "").split("=")

    posx, posy = map(int, _inp[0].split(","))
    velx, vely = map(int, _inp[1].split(","))

    return (posx, posy * -1), (velx, vely * -1)

shrinking = True
elap = 0
plots = []
plotarea = 0

while shrinking:
    plot = ()
    plotx = []
    ploty = []
    for x in inp.splitlines():
        pos, vel = parse(x)

        pos = tuple(map(lambda p, v: p + (v * elap), pos, vel))

        plot += (pos,)

        plotx.append(pos[0])
        ploty.append(pos[1])

    if plotarea < ((max(plotx) - min(plotx)) * (max(plotx) - min(plotx))) and elap > 0:
        shrinking = False
    else:
        plotarea = ((max(plotx) - min(plotx)) * (max(plotx) - min(plotx)))
        plots.append(plot)
        elap += 1

for x in plots[elap-1]:
    plt.scatter(*x)
plt.show()
print(elap-1)


# ----
# Cool Solution
# ----
"""

from inputs.day10 import input as inp
from PIL import Image
from pytesseract import image_to_string

points = []
size = 350
end = 15000

for line in inp.splitlines():
    points.append({
        'x':
            int(line.split("<")[1].split(",")[0].strip()),
        'y':
            int(line.split("<")[1].split(",")[1].split(">")[0].strip()),
        'x_velocity':
            int(line.split("<")[2].split(",")[0].strip()),
        'y_velocity':
            int(line.split("<")[2].split(",")[1].split(">")[0].strip())
    })

time = 0
min_area = None
while True:
    max_x = 0
    max_y = 0
    min_x = size
    min_y = size

    for point in points:
        x = point['x'] + time * point['x_velocity']
        y = point['y'] + time * point['y_velocity']
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    area = abs(max_x - min_x) * abs(max_y - min_y)
    if min_area is None or area < min_area:
        min_area = area
    else:
        time -= 1
        break
    time += 1

text = [[0 for _ in range(max_x - min_x + 1)]
        for _ in range(max_y - min_y + 1)]
for point in points:
    x = (point['x'] + time * point['x_velocity']) - min_x
    y = (point['y'] + time * point['y_velocity']) - min_y
    text[y][x] = 255

img = Image.new('RGB', (len(text[0]), len(text)), "black")
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixels[x, y] = (text[y][x], text[y][x], text[y][x])
# print(image_to_string(img))
img.show()
print("Found at: " + str(time))

"""