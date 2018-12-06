"""
solution for day 1
reading from file
"""

# part 1
# simply read the file

filename = 'input.txt'


def findSum():
    result = 0
    with open(filename, 'r') as f:
        for line in f:
            result += int(line)
        return (result)

# part 2
# keep track of what's been read

import itertools


def findrepeat():
    data = [int(x) for x in open(filename, 'r').readlines()]
    result = 0
    seen = {0}  # optimized for searching through
    for num in itertools.cycle(data):
        result += num
        if result in seen:
            return (result)
        seen.add(result)


print(findrepeat())
