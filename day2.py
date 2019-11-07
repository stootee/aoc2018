from day2_input import inp

# PART 1

twice = 0
thrice = 0

for x in inp.split('\n'):
    seen = set()
    dupes = {}

    for y in list(x):
        if y in seen:
            try:
                dupes[y] += 1
            except:
                dupes[y] = 2
        else:
            seen.add(y)

    twos = False
    threes = False
    for letter, cnt in dupes.items():
        if cnt == 2:
            twos = True
        if cnt == 3:
            threes = True

    if twos:
        twice += 1
    if threes:
        thrice += 1

print(twice * thrice)

# PART 2

new_set = set()
candidates = {}

for x in inp.split('\n'):

    for y in range(0, len(x)):
        test = x[:y] + x[y+1:]
        if (test, y) in new_set:
            print(test)
        else:
            new_set.add((test, y))
            #print (test, y)

# for x in candidates.items():
#     print x
