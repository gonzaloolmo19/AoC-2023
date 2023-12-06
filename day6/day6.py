def parse_input(file):
    with open(file, "r") as f:
        return [line.strip() for line in f.readlines()]


def dist(charging_time, time_total):
    return charging_time * (time_total - charging_time)


def possible_charging_times1(time_total, distance):
    initial = 0
    final = 0
    for i in range(1, time_total):
        if dist(i, time_total) > distance:
            initial = i
            break
    for i in range(time_total - 1, initial, -1):
        if dist(i, time_total) > distance:
            final = i
            break
    return final - initial + 1


# Hace los mismo que la anterior, pero es mas eficiente la anterior en los casos
# del problema
def possible_charging_times2(time_total, distance):
    count = 0
    for i in range(1, time_total):
        if dist(i, time_total) > distance:
            count += 1
    return count


def part1():
    times, distances = parse_input("input.txt")
    _, times = times.split(": ")
    _, distances = distances.split(": ")
    times = times.split()
    distances = distances.split()
    times = [int(time) for time in times]
    distances = [int(distance) for distance in distances]

    solution = 1
    for i in range(len(times)):
        solution *= possible_charging_times1(times[i], distances[i])

    return solution


def part2():
    time, distance = parse_input("input.txt")
    _, time = time.split(": ")
    _, distance = distance.split(": ")
    time = time.replace(" ", "")
    distance = distance.replace(" ", "")

    return possible_charging_times1(int(time), int(distance))


print("Solution for part 1: ", part1())
print("Solution for part 2: ", part2())
