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


print("Part 1: ", part1())
