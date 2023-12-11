def parse_input(file):
    with open(file) as f:
        return [line.replace("\n", "") for line in f.readlines()]


def empty_row(matrix, row):
    for i in range(len(matrix[row])):
        if matrix[row][i] != ".":
            return False
    return True


def empty_col(matrix, j):
    for i in range(len(matrix)):
        if matrix[i][j] != ".":
            return False
    return True


def find_galaxies(matrix):
    galaxies = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "#":
                galaxies.append((i, j))
    return galaxies


def galaxy_distance(galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def part1():
    file = "input.txt"
    space = parse_input(file)

    i = 0
    while i < len(space):
        if empty_row(space, i):
            space = space[:i] + ["." * len(space[0])] + space[i:]
            i += 1
        i += 1

    j = 0
    while j < len(space[0]):
        if empty_col(space, j):
            for i in range(len(space)):
                array_char = list(space[i])
                array_char.insert(j, ".")
                space[i] = "".join(array_char)
            j += 1
        j += 1

    __import__("pprint").pprint(space)
    galaxies = find_galaxies(space)

    suma = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            suma += galaxy_distance(galaxies[i], galaxies[j])

    return suma


print("part1: ", part1())
