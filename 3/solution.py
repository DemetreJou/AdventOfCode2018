import numpy as np

"""
day 3 solutions
"""
filename = 'input.txt'
data = [x for x in open(filename, 'r').readlines()]

# part 1, find the amount of overlap

SIZE = 10000
fabric = np.zeros((SIZE, SIZE))

"""
marks the farbic array based on the input
"""


def extract_information(line):
    claim = line.split()
    id = claim[0][1:]
    pos = claim[2].split(',')  # splits x, y coord
    posx = int(pos[0])
    posy = int(pos[1][:-1])  # removes tailing colon
    size = claim[3].split('x')
    sizex = int(size[0])
    sizey = int(size[1])
    return id, posx, posy, sizex, sizey


def part1(data):
    for line in data:
        id, posx, posy, sizex, sizey = extract_information(line)
        fabric[posx:posx + sizex, posy:posy + sizey] += 1
    return (fabric > 1).sum()


def part2(data):
    result = '69 ;)'
    for line in data:
        id1, posx, posy, sizex, sizey = extract_information(line)
        fabric[posx:posx + sizex, posy:posy + sizey] += 1
    for line in data:
        id2, posx, posy, sizex, sizey = extract_information(line)
        claim = fabric[posx:posx + sizex, posy:posy + sizey]
        if claim.max() == 1:
            result = id2
    return result

# # uncomment each part to find solution
# print(part1(data))
# print(part2(data))
