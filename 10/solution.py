# assuming the words will appear when the area the dots appear in is minimal
# keep moving time forward until the area increases
# display and read the message manually
import fileinput
import re
from itertools import count

# in form (x, y, dx, dy)
data = [tuple(map(int, re.findall(r'[-\d]+', x))) for x in fileinput.input()]


# returns where the stars are at time t
def state(points, t):
    return [(x + dx * t, y + dy * t) for x, y, dx, dy in points]


def bounds(points):
    x0, y0 = min(p[0] for p in points), min(p[1] for p in points)
    x1, y1 = max(p[0] for p in points), max(p[1] for p in points)
    return (x0, y0, x1, y1)


def area(points):
    x0, y0, x1, y1 = bounds(points)
    return (x1 - x0) * (y1 - y0)


def find_min_area(points):
    current_min = area(points)
    for t in count():
        a = area(state(points, t))
        if a > current_min:
            # last time unit was smallest
            return t - 1
        # assuming the area will always get smaller
        current_min = a


# create a string to read the message
def display(points):
    x0, y0, x1, y1 = bounds(points)
    points = set(points)
    rows = []
    for y in range(y0, y1 + 1):
        row = []
        for x in range(x0, x1 + 1):
            row.append('0' if (x, y) in points else ' ')
        rows.append(''.join(row))
    return '\n'.join(rows)


t = find_min_area(data)
print(display(state(data, t)))
# solution reads LKPHZHHJ

print(t)
