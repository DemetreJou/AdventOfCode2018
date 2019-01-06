# cellular automaton again
import fileinput
from collections import Counter
from itertools import count

lines = [line.strip() for line in fileinput.input()]


# as normal parse into a dictionary from (x,y) to char at that point
# legend:
# . = open
# | = tree
# # = lumberyard
def make_grid(lines):
    grid = {}
    w, h = len(lines[0]), len(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return w, h, grid


# moves forwards one time unit (in this case it's discrete minutes)
def step(w, h, grid):
    # since the entire grid updates at the same time (instead of scanning across rows)
    # we return a new grid
    # so the new grid isn't affected by a partially updated grid
    result = {}
    for y in range(h):
        for x in range(w):
            # scanning rows then columns
            c = grid[(x, y)]
            # find all 8 neighbours
            neighbours = [grid.get((x + dx, y + dy), '') for dy in range(-1, 2) for dx in range(-1, 2) if dy or dx]
            # find what to update current spot based on rules and neighbours
            counts = Counter(neighbours)
            if c == '.':
                if counts['|'] >= 3:
                    c = '|'
            # save into the new grid
            elif c == '|':
                if counts['#'] >= 3:
                    c = '#'
            elif c == '#':
                if counts['#'] == 0 or counts['|'] == 0:
                    c = '.'
            # possibility of nothing happening
            result[(x, y)] = c
    return result


def recoure_value(grid):
    counts = Counter(grid.values())
    return counts['|'] * counts['#']


# simulate 10 steps
def part1():
    w, h, grid = make_grid(lines)
    for i in range(10):
        grid = step(w, h, grid)
    return print(recoure_value(grid))


# similar to previous day, must find pattern instead of simulating 1 trillion steps
def part2():
    w, h, grid = make_grid(lines)
    seen = {}
    prev = 0
    for i in count(1):
        grid = step(w, h, grid)
        v = recoure_value(grid)
        cycle = i - seen.get(v, 0)
        if cycle == prev:
            if 1000000000 % cycle == i % cycle:
                print(recoure_value(grid))
                break
        seen[v] = i
        prev = cycle


part1()
part2()
