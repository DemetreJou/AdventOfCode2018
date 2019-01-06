import fileinput
import re


# water falling down is fall
# water spreading horizontally is scan


class Model:
    """
    Models the underground area
    Keeps track of clay, falling water, still water
    """

    def __init__(self, lines):
        self.clay = set()  # (x,y) clay position
        self.still = set()  # (x,y) still water positions
        self.flowing = set()  # (x,y) flowing (falling) water position

        # parse the lines (the input)
        for line in lines:
            # lines are in form x,y = a, y,x = b0 .... b1
            a, b0, b1 = map(int, re.findall(r'\d+', line))
            for b in range(b0, b1 + 1):
                # line could be in form x,y or y,x
                # ensure it's saved in form of (x,y)
                self.clay.add((a, b) if line[0] == 'x' else (b, a))
        # find bounds to count within
        self.x0 = min(x for x, y in self.clay)
        self.x1 = max(x for x, y in self.clay)
        self.y0 = min(y for x, y in self.clay)
        self.y1 = max(y for x, y in self.clay)
        self.queue = []

    def __init__(self, lines):
        self.clay = set()
        self.still = set()
        self.flowing = set()
        for line in lines:
            a, b0, b1 = map(int, re.findall(r'\d+', line))
            for b in range(b0, b1 + 1):
                self.clay.add((a, b) if line[0] == 'x' else (b, a))
        self.x0 = min(x for x, y in self.clay)
        self.x1 = max(x for x, y in self.clay)
        self.y0 = min(y for x, y in self.clay)
        self.y1 = max(y for x, y in self.clay)
        self.queue = []

    def run(self, x, y):
        self.queue.append((self.fall, x, y))
        while self.queue:
            func, *args = self.queue.pop()
            func(*args)

    def count_all(self):
        return sum(1 for x, y in self.still | self.flowing
                   if y >= self.y0 and y <= self.y1)

    def count_still(self):
        return sum(1 for x, y in self.still
                   if y >= self.y0 and y <= self.y1)

    def stop(self, x, y):
        return (x, y) in self.clay

    def pile(self, x, y):
        return (x, y) in self.clay or (x, y) in self.still

    def fall(self, x, y):
        while y <= self.y1 and not self.pile(x, y + 1):
            self.flowing.add((x, y))
            y += 1
        if y <= self.y1:
            self.flowing.add((x, y))
            self.queue.append((self.scan, x, y))

    def scan(self, x, y):
        x0 = x
        while self.pile(x0, y + 1) and not self.stop(x0 - 1, y):
            x0 -= 1
        x1 = x
        while self.pile(x1, y + 1) and not self.stop(x1 + 1, y):
            x1 += 1
        stop0 = self.stop(x0 - 1, y)
        stop1 = self.stop(x1 + 1, y)
        if stop0 and stop1:
            for i in range(x0, x1 + 1):
                self.still.add((i, y))
            self.queue.append((self.scan, x, y - 1))
        else:
            for i in range(x0, x1 + 1):
                self.flowing.add((i, y))
            if not stop0:
                self.queue.append((self.fall, x0, y))
            if not stop1:
                self.queue.append((self.fall, x1, y))


model = Model(fileinput.input())
model.run(500, 0)
print(model.count_all())
print(model.count_still())
