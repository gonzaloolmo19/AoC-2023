def parse_input(file):
    with open(file, "r") as f:
        return [[int(x) for x in line.strip().split()] for line in f.readlines()]


def get_prediction(line) -> int:
    triangulo = []
    triangulo.append(line)
    todos_cero = False
    num_lineas = 1
    prediciones = [0]

    while not todos_cero:
        triangulo.append([])
        num_lineas += 1
        for i in range(len(triangulo[num_lineas - 2]) - 1):
            triangulo[num_lineas - 1].append(
                triangulo[num_lineas - 2][i + 1] - triangulo[num_lineas - 2][i]
            )

        todos_cero = True
        for num in triangulo[num_lineas - 1]:
            if num != 0:
                todos_cero = False
                break

    for i in range(num_lineas - 2, -1, -1):
        print("aniadiendo: ", triangulo[i][-1], "+", prediciones[-1])
        prediciones.append(triangulo[i][-1] + prediciones[-1])

    print("Predicciones: ", prediciones)
    return prediciones[-1]


def part1():
    file = "input.txt"
    lines = parse_input(file)
    print("Lines:  ", lines)

    suma = 0

    for line in lines:
        suma += get_prediction(line)

    return suma


print("Part 1: ", part1())
