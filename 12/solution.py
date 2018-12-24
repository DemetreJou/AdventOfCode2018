# this is a cellular automaton of size 5
# and rules are given in the input
# where '#' is on and '.' is off
import fileinput

lines = list(fileinput.input())

# set up initial state
# set of locations where a plant (cell) is
initial_state = set(i for i, x in enumerate(lines[0].split()[-1]) if x == '#')

# define rules
# function that takes in a central location + 2 locations to either side and decides what happens at that location

rules = dict(line.split()[::2] for line in lines[2:])


# moves the entire system one time unit over based on rules
def step(state) -> set:
    result = set()
    # checks everything in view of any active cell ( 2 to either side)
    for i in range(min(state) - 2, max(state) + 3):
        # construct a 5 length string to match to rules
        sub_section = ''.join('#' if j in state else '.' for j in range(i - 2, i + 3))
        # check if any rules apply to this section
        if rules[sub_section] == '#':
            result.add(i)

    return result


# see what state occurs after 20 iterations
def part1():
    s = initial_state
    for i in range(20):
        s = step(s)
    print(sum(s))


# 50 billion number is too large to simulate
# assume that it eventually reaches some equilibrium after 500 iteration
def part2():
    s = initial_state
    p = n = 0
    for i in range(500):
        p = n
        s = step(s)
        n = sum(s)
    print(p + (n - p) * (50000000000 - i))


part1()
part2()
