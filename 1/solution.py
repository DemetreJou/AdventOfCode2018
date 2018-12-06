"""
solution for day 1
reading from file
"""

# part 1

filename = 'input.txt'
result = 0
with open(filename, 'r') as f:
    for line in f:
        result += int(line)
    print(result)

# part 2
