"""429 players; last marble is worth 70901 points"""
from collections import deque

players = 429
last_marble_value = 70901 * 100

circle = deque([0])


def move_pointer(_current, jumps=0):
    idx = circle.index(_current)

    new_idx = (idx + jumps) % len(circle)

    return circle[new_idx], new_idx


def place_marble(_marble_value, _current):
    _score = 0

    if _marble_value % 23 == 0:
        _scoring_marble, _index = move_pointer(_current, -7)

        _score = _marble_value + _scoring_marble

        del circle[_index]

        _current = circle[_index]

    else:
        a, _index = move_pointer(_current, 2)
        circle.insert(_index, _marble_value)
        _current = _marble_value

    return _current, _score, _index


marble_value = 1
current = 0
player = 1
players_dict = {}
for x in range(players):
    players_dict[x + 1] = 0

while marble_value <= last_marble_value:
    current, score, index = place_marble(marble_value, current)
    marble_value += 1
    players_dict[player] += score
    player += 1
    if player > players:
        player = 1
    perc_done = marble_value / last_marble_value * 100
    if marble_value % 10000 == 0:
        print(marble_value, marble_value / last_marble_value * 100)

print(max(players_dict.values()))



