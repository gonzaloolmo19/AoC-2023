from functools import reduce


def parse_node(line: str):
    line = line.replace(" ", "")
    name, options = line.split("=")
    options = options.replace("(", "").replace(")", "").split(",")
    return [name, options]


def parse_input(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
        return [lines[0], lines[2:]]


def part1():
    file = "input.txt"
    instructions, nodes = parse_input(file)
    nodes = [parse_node(node) for node in nodes]

    direction = {"L": 0, "R": 1}
    # Create a map of the nodes
    map = {}
    for node in nodes:
        map[node[0]] = node[1]

    node = map["AAA"][direction[instructions[0]]]
    count = 1
    while node != "ZZZ":
        node = map[node][direction[instructions[count % len(instructions)]]]
        count += 1

    return count


def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mcm(a, b):
    return (a * b) // mcd(a, b)


def part2():
    file = "input.txt"
    instructions, nodes = parse_input(file)
    nodes = [parse_node(node) for node in nodes]

    direction = {"L": 0, "R": 1}
    # Create a map of the nodes
    map = {}
    for node in nodes:
        map[node[0]] = node[1]

    # Find all nodes ending with 'A'
    checking_nodes = [node for node in map if node.endswith("A")]

    count = 0
    end_Z = []
    top = len(checking_nodes)
    while len(end_Z) < top:
        for i in range(len(checking_nodes)):
            checking_nodes[i] = map[checking_nodes[i]][
                direction[instructions[count % len(instructions)]]
            ]
        count += 1
        for node in checking_nodes:
            if node.endswith("Z"):
                end_Z.append(count)
                checking_nodes.remove(node)

    return reduce(mcm, end_Z)


print("Part 1: ", part1())
print("Part 2: ", part2())
