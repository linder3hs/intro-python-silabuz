# Ejemplo de generador
def funcion_generador(collection):
    for i in collection:
        if i % 2 == 0:
            yield i * 2
        else:
            yield i + 1


numeros = [1, 2, 3, 4, 5]


# funcion_generador
# lo que retorna siempre es un iterable
print(list(funcion_generador(numeros)))
