import fileinput

# first time using a class!
# each cart object represents what turn cycle it's on
# where it is
# has method to move and check collision

# define up, down, left, right directions for ease
U, D, L, R = (0, -1), (0, 1), (-1, 0), (1, 0)

# convert symbols to directions
directions = {'^': U, 'v': D, '<': L, '>': R}

# maps for directions
straight = {U: U, D: D, L: L, R: R}
left_turn = {U: L, D: R, L: D, R: U}
right_turn = {U: R, D: L, L: U, R: D}
forward_slash_turn = {U: R, D: L, L: D, R: U}
back_slash_turn = {U: L, D: R, L: U, R: D}


class Cart:
    def __init__(self, p, d):
        # p and d are in the form (x,y)
        self.p = p
        self.d = d
        self.turns = 0
        self.ok = True

    def step(self, grid):
        # moves one step
        self.p = (self.p[0] + self.d[0], self.p[1] + self.d[1])
        # adds card to grid
        c = grid[self.p]
        # if at intersection figure out turn
        if c == '+':
            turn = [left_turn, straight, right_turn][self.turns % 3]  # turns are in cycles of 3
            self.d = turn[self.d]  # apply appropriate turn
            self.turns += 1
        elif c == '/':
            self.d = forward_slash_turn[self.d]
        elif c == '\\':
            self.d = back_slash_turn[self.d]

    def collide(self, other):
        # returns True if two cards collide
        return self != other and self.ok and other.ok and self.p == other.p


print('0')

# populate the grid
grid = {}  # grid maps (x, y) positions to characters from the input
carts = []  # carts is a list of Cart instances
for y, line in enumerate(fileinput.input()):
    for x, c in enumerate(line):
        grid[(x, y)] = c
        if c in directions:
            carts.append(Cart((x, y), directions[c]))

# it solves both parts at same time
# easier to run simulation once and just keep track of part 1 while doing part 2
part1 = part2 = None
while True:
    # for each new tick, sort the carts by Y and then X
    carts = sorted(carts, key=lambda x: (x.p[1], x.p[0]))
    for cart in carts:
        # update this cart
        cart.step(grid)
        # check for collisions
        for other in carts:
            if cart.collide(other):
                cart.ok = other.ok = False
                # first collision is our part 1 result
                part1 = part1 or cart.p
    # remove carts that crashed
    carts = [x for x in carts if x.ok]
    # if only one cart is left, part 2 is done
    if len(carts) == 1:
        part2 = carts[0].p
        break

print(part1)
print(part2)
