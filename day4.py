from day4_input import inp
from datetime import datetime
from collections import Counter

shifts = {}

for x in inp.split('\n'):
    _dt = shifts[datetime.strptime(x[1:17], "%Y-%m-%d %H:%M")] = x[19:]


guards = {}
asleep = None
minutes_asleep = []
guard = None
for x in sorted(shifts.keys()):
    print x, shifts[x]
    if "Guard" in shifts[x]:
        guard = shifts[x].replace('begins shift', '')[7:]

    if "asleep" in shifts[x]:
        asleep = x

    if "wakes" in shifts[x]:
        time_asleep = x - asleep
        minutes_asleep = []

        for y in range(0, int(time_asleep.total_seconds() / 60)):
            minutes_asleep.append(y + asleep.minute)

        print minutes_asleep

        try:
            guards[guard]['time_asleep'] += len(minutes_asleep)
            guards[guard]['minutes_asleep'] += minutes_asleep
        except:
            guards[guard] = {
                'time_asleep': len(minutes_asleep),
                'minutes_asleep': minutes_asleep
            }

sleepiest_guard = (None, None)
for x in guards:

    if guards[x]['time_asleep'] > sleepiest_guard[1]:
        sleepiest_guard = (x, guards[x]['time_asleep'])

print sleepiest_guard[0]
print Counter(guards[sleepiest_guard[0]]['minutes_asleep']).most_common(1)

print int(sleepiest_guard[0]) * Counter(guards[sleepiest_guard[0]]['minutes_asleep']).most_common(1)[0][0]

# part2
guard_sleepiest_minute = {}
guard_most_asleep_minute = (None, None, None)
for x in guards:
    most_common_min = Counter(guards[x]['minutes_asleep']).most_common(1)[0]
    if most_common_min[1] > guard_most_asleep_minute[2]:
        guard_most_asleep_minute = (x, most_common_min[0], most_common_min[1])

print guard_most_asleep_minute
print int(guard_most_asleep_minute[0]) * guard_most_asleep_minute[1]




