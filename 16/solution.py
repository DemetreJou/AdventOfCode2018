import fileinput
import re


# lots of definitions for all the different functions
def addr(r, a, b, c): r[c] = r[a] + r[b]


def addi(r, a, b, c): r[c] = r[a] + b


def mulr(r, a, b, c): r[c] = r[a] * r[b]


def muli(r, a, b, c): r[c] = r[a] * b


def banr(r, a, b, c): r[c] = r[a] & r[b]


def bani(r, a, b, c): r[c] = r[a] & b


def borr(r, a, b, c): r[c] = r[a] | r[b]


def bori(r, a, b, c): r[c] = r[a] | b


def setr(r, a, b, c): r[c] = r[a]


def seti(r, a, b, c): r[c] = a


def gtir(r, a, b, c): r[c] = int(a > r[b])


def gtri(r, a, b, c): r[c] = int(r[a] > b)


def gtrr(r, a, b, c): r[c] = int(r[a] > r[b])


def eqir(r, a, b, c): r[c] = int(a == r[b])


def eqri(r, a, b, c): r[c] = int(r[a] == b)


def eqrr(r, a, b, c): r[c] = int(r[a] == r[b])


functions = [
    addr, addi, mulr, muli, banr, bani, borr, bori,
    setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr,
]


# pulls out 'opcode A, B, C' from the line
def parse(line):
    return list(map(int, re.findall(r'\d+', line)))


# finds how many functions match the oberserved behavior
def behaves_like(instruction, before, after):
    count = 0
    for f in functions:
        r = list(before)
        f(r, *instruction[1:])
        if r == after:
            count += 1
    return count


# similar to behaves_like but removes instead
def remove_candidate(instruction, before, after, candidates):
    for f in functions:
        r = list(before)
        f(r, *instruction[1:])
        if r != after:
            candidates[instruction[0]].discard(f)


lines = list(fileinput.input())


# count how many examples behave like 3 or more functions
def part1():
    count = 0
    for line in lines:
        if 'Before' in line:
            before = parse(line)
        elif 'After' in line:
            after = parse(line)
            if behaves_like(instruction, before, after) >= 3:
                count += 1
        else:
            instruction = parse(line)
    return print(count)


part1()
