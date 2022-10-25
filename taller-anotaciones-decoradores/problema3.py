def duplicar_letras() -> list:
    palabra: str = input("Ingrese una palabra: ")
    cantidad_inicial: int = len(palabra)
    duplicando_palabra: str = palabra * 2

    res: list = []
    count: int = 1

    for p in duplicando_palabra:
        if count > cantidad_inicial:
            res.insert(res.index(p) + 1, p)
        else:
            res.append(p)
        count += 1

    return res


print(duplicar_letras())
