from collections import defaultdict
import re
import fileinput

p = [tuple(map(int, re.findall(r'\d+', x))) for x in fileinput.input()]

# find bounds on grid size
x0, x1 = min(x for x, y in p), max(x for x, y in p)
y0, y1 = min(y for x, y in p), max(y for x, y in p)


def distance(x1, y1, x2, y2) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    counts = defaultdict(int)
    inf = set()
    # iterate over the grid
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            ds = sorted((distance(x, y, px, py), i) for i, (px, py) in enumerate(p))
            if ds[0][0] != ds[1][0]:
                counts[ds[0][1]] += 1
                # keep track of what's on edge
                if x == x0 or y == y0 or x == x1 or y == y1:
                    inf.add(ds[0][1])

    # if there is a value on the edge it's area is infinite so remove
    for i in inf:
        counts.pop(i)
    print(max(counts.values()))


def part2():
    pass


part1()
