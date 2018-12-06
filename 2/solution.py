"""
solutions for day 2
"""

# part 1
#
filename = 'input.txt'


def find2letter(string: str):
    for c in string:
        if string.count(c) == 2:
            return True
    return False


def find3letter(string: str):
    for c in string:
        if string.count(c) == 3:
            return True
    return False


def countall():
    result = 0
    amountoftwo = 0
    amountofthree = 0

    data = [x for x in open(filename, 'r').readlines()]

    for i in data:
        amountoftwo += find2letter(i)
        amountofthree += find3letter(i)

    result = amountoftwo * amountofthree
    return result


# print(countall())

# part 2

def checkall():
    data = [x for x in open(filename, 'r').readlines()]

    for x in data:
        for y in data:
            diff = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    diff += 1
            if diff == 1:
                return findincommon(x, y)


def findincommon(x, y):
    result = ''
    for i in range(len(x)):
        if x[i] == y[i]:
            result += x[i]
    return result

# print(checkall())
