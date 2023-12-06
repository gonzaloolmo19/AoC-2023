def parse_input(file):
    with open(file) as f:
        return [x for x in f.read().split("\n\n")]


def remove_all(list, element):
    return [x for x in list if x != element]


def parse_map(map):
    b, seeds = map.split(":")
    seeds = seeds.split("\n")
    seeds = remove_all(seeds, "")

    for i in range(len(seeds)):
        seeds[i] = seeds[i].split(" ")
        seeds[i] = remove_all(seeds[i], "")

    return seeds


def build_map(list):
    map = {}

    for i in range(len(list)):
        for j in range(list[i][2]):
            map[list[i][1] + j] = list[i][0] + j
            print(list[i][1] + j, list[i][0] + j)
    return map


def part1():
    file = "input.txt"
    (
        seeds,
        seed_to_soil,
        soil_to_fert,
        fert_to_water,
        water_to_ligth,
        light_to_temp,
        temp_to_hum,
        hum_to_loc,
    ) = parse_input(file)

    seeds = parse_map(seeds)
    seeds = [list(map(int, x)) for x in seeds]
    seed_to_soil = parse_map(seed_to_soil)
    seed_to_soil = [list(map(int, x)) for x in seed_to_soil]
    soil_to_fert = parse_map(soil_to_fert)
    soil_to_fert = [list(map(int, x)) for x in soil_to_fert]
    fert_to_water = parse_map(fert_to_water)
    fert_to_water = [list(map(int, x)) for x in fert_to_water]
    water_to_ligth = parse_map(water_to_ligth)
    water_to_ligth = [list(map(int, x)) for x in water_to_ligth]
    light_to_temp = parse_map(light_to_temp)
    light_to_temp = [list(map(int, x)) for x in light_to_temp]
    temp_to_hum = parse_map(temp_to_hum)
    temp_to_hum = [list(map(int, x)) for x in temp_to_hum]
    hum_to_loc = parse_map(hum_to_loc)
    hum_to_loc = [list(map(int, x)) for x in hum_to_loc]

    mapas = [
        seed_to_soil,
        soil_to_fert,
        fert_to_water,
        water_to_ligth,
        light_to_temp,
        temp_to_hum,
        hum_to_loc,
    ]

    # Vamos a intentar obtener la localizacion a partir de una semilla
    location_list = []

    for i in range(len(seeds[0])):
        clave = seeds[0][i]
        for j in range(len(mapas)):
            for k in range(len(mapas[j])):
                if clave in range(mapas[j][k][1], mapas[j][k][2] + mapas[j][k][1]):
                    clave = mapas[j][k][0] + (clave - mapas[j][k][1])
                    break

        location_list.append(clave)

    return min(location_list)


def part2():
    file = "input.txt"
    (
        seeds,
        seed_to_soil,
        soil_to_fert,
        fert_to_water,
        water_to_ligth,
        light_to_temp,
        temp_to_hum,
        hum_to_loc,
    ) = parse_input(file)

    seeds = parse_map(seeds)
    seeds = [list(map(int, x)) for x in seeds]
    seed_to_soil = parse_map(seed_to_soil)
    seed_to_soil = [list(map(int, x)) for x in seed_to_soil]
    soil_to_fert = parse_map(soil_to_fert)
    soil_to_fert = [list(map(int, x)) for x in soil_to_fert]
    fert_to_water = parse_map(fert_to_water)
    fert_to_water = [list(map(int, x)) for x in fert_to_water]
    water_to_ligth = parse_map(water_to_ligth)
    water_to_ligth = [list(map(int, x)) for x in water_to_ligth]
    light_to_temp = parse_map(light_to_temp)
    light_to_temp = [list(map(int, x)) for x in light_to_temp]
    temp_to_hum = parse_map(temp_to_hum)
    temp_to_hum = [list(map(int, x)) for x in temp_to_hum]
    hum_to_loc = parse_map(hum_to_loc)
    hum_to_loc = [list(map(int, x)) for x in hum_to_loc]

    mapas = [
        seed_to_soil,
        soil_to_fert,
        fert_to_water,
        water_to_ligth,
        light_to_temp,
        temp_to_hum,
        hum_to_loc,
    ]

    # Vamos a intentar obtener la localizacion a partir de una semilla
    location_list = []
    min = 10000000000000000000000000000

    for i in range(0, len(seeds[0]), 2):
        for ind_clave in range(i, i + seeds[0][i + 1]):
            clave = seeds[0][i] + ind_clave - i
            for j in range(len(mapas)):
                for k in range(len(mapas[j])):
                    if clave in range(mapas[j][k][1], mapas[j][k][2] + mapas[j][k][1]):
                        clave = mapas[j][k][0] + (clave - mapas[j][k][1])
                        break

            if clave < min:
                min = clave
            print(min)

    return min


print("Resultado parte 1:", part1())
print("Resultado parte 2:", part2())
