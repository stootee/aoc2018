from day3_input import inp as inp

claims = {}

for x in inp.split('\n'):
    splits = x.split(" ")
    claims[splits[0]] = (splits[2].replace(":", "").split(","), splits[3].split("x"), 0)


def patches(coords, size):
    patch = []
    for w in range(0, int(size[0])):
        for h in range(0, int(size[1])):
            patch.append((int(coords[0]) + w, int(coords[1]) + h))

    return patch

claimed = {}
for id, dimensions in claims.items():
    overlap = False
    for x in patches(dimensions[0], dimensions[1]):
        try:
            claimed[x].append(id)
            overlap = True
        except:
            claimed[x] = [id]

overlap = 0
for coord, ids in claimed.items():
    if len(ids) > 1:
        overlap += 1

print overlap

# PART 2

aaa = {}
for coord, ids in claimed.items():
    for x in ids:
        if len(ids) == 1:
            try:
                aaa[x] += 1
            except:
                aaa[x] = 1


for id, dimensions in claims.items():
    try:
        if int(dimensions[1][0]) * int(dimensions[1][1]) == aaa[id]:
            print id
    except:
        pass




