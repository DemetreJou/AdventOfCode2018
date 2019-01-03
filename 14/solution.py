import fileinput

# this puzzle was very confusing
# good thing python is basically english
# however code was straightforward

n = int(next(fileinput.input()))


# given current list of scores and current elves return the elves
def step(scores, i, j):
    # scores of both elves
    s = scores[i] + scores[j]
    # s is from 0 to 19
    if s >= 10:
        scores.append(1)
    scores.append(s % 10)
    # move elves
    i = (i + scores[i] + 1) % len(scores)  # moves around and loops if necesary
    j = (j + scores[j] + 1) % len(scores)
    return (i, j)


def part1():
    # initial condition from question
    scores, i, j = [3, 7], 1, 0
    while len(scores) < n + 10:
        i, j = step(scores, i, j)
    # print the last 10 scores
    print(''.join(map(str, scores[n:n + 10])))


def part2():
    scores, i, j = [3, 7], 1, 0
    digits = list(map(int, str(n)))
    # see if the last N digits match input
    # check last and second to last as we could have added 2 new numbers at the end
    while True:
        i, j = step(scores, i, j)
        if scores[-len(digits) - 1:-1] == digits:
            print(len(scores) - len(digits) - 1)
            break
        if scores[-len(digits) - 1:] == digits:
            print(len(scores) - len(digits))
            break


part1()
part2()
