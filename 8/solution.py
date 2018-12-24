import fileinput


def parse(input) -> tuple:
    # from iterating over the input
    num_children, num_metadata = next(input), next(input)
    # find all children
    children = [parse(input) for _ in range(num_children)]
    # finding metadata of the children
    metadata = [next(input) for _ in range(num_metadata)]
    return (metadata, children)


root = parse(map(int, next(fileinput.input()).split()))


def part1(node):
    # sums all the metadata
    metadata, children = node
    return sum(metadata) + sum(part1(x) for x in children)


def part2(node):
    metadata, children = node
    if children:
        return sum(part2(children[i - 1]) for i in metadata if 1 <= i <= len(children))
    return sum(metadata)


print(part1(root))
print(part2(root))
