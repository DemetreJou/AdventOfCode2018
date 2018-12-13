from string import *

"""
solution for day 5
"""

line = open('input.txt').read().strip()
oldline = None


def collapse(s):
    result = ['.']
    for c in s:  # c is character were looking at
        v = result[-1]  # the last character we've looked at
        if c != v and c.lower() == v.lower():
            result.pop()
        else:
            result.append(c)
    return len(result) - 1


print(collapse(line))
# where all_possible is line with a different lower case letter removed each time
all_possible = [[a for a in line if a.lower() != x] for x in ascii_lowercase]
print(min(collapse(x) for x in all_possible))
