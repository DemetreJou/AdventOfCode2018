"""
solutions to day 4
"""
from collections import defaultdict

data = open('input.txt', 'r').readlines()
data.sort()

C = defaultdict(int)
CM = defaultdict(lambda: defaultdict(int))


def parse_time(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])


def find_asleep():
    guard_id = None
    asleep = None
    for line in data:
        time = parse_time(line)
        if "begins shift" in line:
            guard_id = int(line.split()[3][1:])
            asleep = None
        elif "falls" in line:
            asleep = time
        elif "wakes up" in line:
            for t in range(asleep, time):
                CM[guard_id][t] += 1
                C[guard_id] += 1


def argmax(d):
    best = None
    for i, j in d.items():
        if best is None or j > d[best]:
            best = i
    return best


# uncomment for part 1
find_asleep()
best_guard = argmax(C)
best_min = argmax(CM[best_guard])
print(best_guard * best_min)
