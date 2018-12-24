from collections import defaultdict
import re
import fileinput

# set up and parsa the data
# all tasks are names A - Z
tasks = set()
dependency = defaultdict(set)
for line in fileinput.input():
    a, b = re.findall(r' ([A-Z]) ', line)
    # a must occur before b
    tasks |= {a, b}
    # b depends on a
    dependency[b].add(a)


def part1():
    finished = []
    for _ in tasks:
        # find the earliest alphabetical task that isn't done yet and task that can be done
        finished.append(min(x for x in tasks if x not in finished and dependency[x] <= set(finished)))
    print(''.join(finished))


def part2():
    finished = set()
    # total time in seconds
    seconds = 0
    # how long for worker 'i' to finished their current task
    counts = [0] * 5
    # which task worker 'i' is performing
    work = [''] * 5
    while True:
        # update workers time
        # if finished update task as finished
        for i, count in enumerate(counts):
            if count == 1:
                finished.add(work[i])
            counts[i] = max(0, count - 1)
        while 0 in counts:
            # find idle worker
            i = counts.index(0)
            # find task that can be performed
            candidate = [x for x in tasks if dependency[x] <= finished]
            # no more tasks to be done end loop
            if not candidate:
                break
            # earleir alphabetical task
            task = min(candidate)
            tasks.remove(task)
            # worker starts new task
            counts[i] = ord(task) - ord('A') + 61
            work[i] = task
        if sum(counts) == 0:
            break
        seconds += 1
    print(seconds)

# uncomment to run
# part1()
# part2()
