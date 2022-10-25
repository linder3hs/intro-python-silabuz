# Dada la siguiente lista['Hola', True, 5, 6.04]

# Imprimir los valores e índices sin utilizar un contador o range.
lista = ['Hola', True, 5, 6.04]

# nota: Por default enumerate empieza a contar desde el numero 0

for contador, i in enumerate(lista, start=10):
    # count va a ser el indice generate enumerate
    # i es el valor
    print(contador, "->", i)
