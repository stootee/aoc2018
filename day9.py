"""429 players; last marble is worth 70901 points"""

players = 13
last_marble_value = 7999

circle = [0]


def place_marble(_marble_value, _current):
    _index = circle.index(_current)
    _score = 0

    if _marble_value % 23 == 0:
        if _index >= 7:
            _index = _index - 7
        else:
            _index = len(circle) + (_index - 7)

        _score = _marble_value + circle[_index]

        circle.pop(_index)

        if _index + 1 == len(circle):
            _current = circle[0]
        else:
            _current = circle[_index]

    else:
        if _index + 1 == len(circle):
            _index = 1
        else:
            _index = _index + 2

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
    # print(player, marble_value, current, score, circle)
    marble_value += 1
    # if score > 0:
    #     input("Player scored!!!! Enter to continue...")
    players_dict[player] += score
    player += 1
    if player > players:
        player = 1

print(max(players_dict.values()))



