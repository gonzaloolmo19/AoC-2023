import re


file_path = "input.txt"
with open(file_path) as f:
    lines = f.readlines()

    numeros = re.findall(r"\d+", lines[0])
    print(numeros)

    simbolos = "*/?!@#$%^&*-_=+"
    pos_simbolos_anterior = []
    pos_simbolos_actual = []

    for i in range(len(lines[0])):
        if lines[0][i] in simbolos:
            pos_simbolos_actual.append(i)

    suma = 0
    for i in range(len(lines)):
        numeros = re.findall(r"\d+", lines[i])
        pos_numeros = []
        # for a in range(len(numeros)):
        # if lines[i].find("." + numeros[a] + ".") != -1:
        #     pos_numeros.append(lines[i].find(numeros[a]))

        for coincidencia in re.finditer(r"\d+", lines[i]):
            pos_numeros.append(coincidencia.start())

        pos_simbolos_siguiente = []
        if i + 1 < len(lines):
            for j in range(len(lines[i + 1])):
                if lines[i + 1][j] in simbolos:
                    pos_simbolos_siguiente.append(j)

        encontrado = False
        for n in range(len(pos_numeros)):
            encontrado = False
            for p in pos_simbolos_anterior:
                if (
                    p in range(pos_numeros[n] - 1, pos_numeros[n] + len(numeros[n]) + 1)
                    and not encontrado
                ):
                    print(numeros[n])
                    suma += int(numeros[n])
                    encontrado = True

            for p in pos_simbolos_actual:
                if (
                    p in range(pos_numeros[n] - 1, pos_numeros[n] + len(numeros[n]) + 1)
                    and not encontrado
                ):
                    print(numeros[n])
                    suma += int(numeros[n])
                    encontrado = True

            for p in pos_simbolos_siguiente:
                if (
                    p in range(pos_numeros[n] - 1, pos_numeros[n] + len(numeros[n]) + 1)
                    and not encontrado
                ):
                    print(numeros[n])
                    suma += int(numeros[n])
                    encontrado = True

        # print("pos_numeros", i, pos_numeros)
        # print("pos simbolos anterior", pos_simbolos_anterior)
        # print("pos simbolos actual", pos_simbolos_actual)
        # print("pos simbolos siguiente", pos_simbolos_siguiente)

        pos_simbolos_anterior = pos_simbolos_actual
        pos_simbolos_actual = pos_simbolos_siguiente

    print("Suma", suma)
