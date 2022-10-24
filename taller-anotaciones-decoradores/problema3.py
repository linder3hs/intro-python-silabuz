def duplicar_letras() -> list:
    palabra: str = input("Ingrese una palabra: ")
    cantidad_inicial: int = len(palabra)
    duplicando_palabra: str = palabra * 2

    res: list = []
    count: int = 1
    operando = 0

    for p in duplicando_palabra:
        if count > cantidad_inicial:
            operando += count
            res.insert(operando, p)
            operando = count
        else:
            res.insert(count, p)

        count += 1

    return res
    # palabra: str = input("Ingrese una palabra: ")
    # res: list = []
    # for p in palabra:
    #     res.append(p)
    #     res.append(p)

    # return res


print(duplicar_letras())
