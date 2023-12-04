
def parse_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


def parse_line(line: str):
    line.strip()
    line_split = line.split(":")
    card = line_split[1].split("|")
    card[1] = card[1].strip()
    card[0] = card[0].strip()

    return card


def remove_all(lista, elemento):
    return [i for i in lista if i != elemento]


def get_winning_num(card):
    winning = card[0].split(" ")
    return remove_all(winning, "")


def get_card_num(card):
    num = card[1].split(" ")
    return remove_all(num, "")


def part1():
    lines = parse_input()

    suma = 0
    for line in lines:
        card = parse_line(line)
        winning_num = get_winning_num(card)
        card_num = get_card_num(card)

        encontrado = False
        sumando = 0
        for num in card_num:
            if num in winning_num and not encontrado:
                sumando = 1
                encontrado = True
            elif num in winning_num and encontrado:
                sumando *= 2
        suma += sumando

    print("Part 1:", suma)

def sumatorio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def part2():
    lines = parse_input()

    scratch_cards = []
    for i in range(len(lines)):
        scratch_cards.append(1)
        
    contador =0
    for line in lines:
        card = parse_line(line)
        winning_num = get_winning_num(card)
        card_num = get_card_num(card)

        encontrados=0
        for num in card_num:
            if num in winning_num:
                encontrados+=1

        for i in range(contador+1, contador+encontrados+1):
            if i < len(scratch_cards):
                scratch_cards[i] +=  scratch_cards[contador]

        contador +=1

    print("Part 2:", sumatorio(scratch_cards))

part1()
part2()
