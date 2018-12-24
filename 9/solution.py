# deque.rotate(n) shifts everything n units to the right
from collections import deque
import fileinput
import re

# reads the only two numbers
num_players, num_marbles = map(int, re.findall(r'\d+', next(fileinput.input())))


def playgame(num_players, num_marbles):
    circle = deque([0])
    scores = [0] * num_players
    for i in range(1, num_marbles + 1):
        if i % 23 == 0:
            circle.rotate(7)
            # updates respective score
            scores[i % num_players] += i + circle.pop()
            # rotate left by 1
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)

    return max(scores)


print(playgame(num_players, num_marbles))
print(playgame(num_players, num_marbles * 100))
