# Escriba un generador que permita contar las letras de las palabras de una lista.

# Ejemplos:

# Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}

# Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}

def contador_palabras(word):
    return {i: word.count(i) for i in word}


print(contador_palabras("humanidad"))
print(contador_palabras("humano"))

# Nota: Es posible usar return en un generador, pero ojo
# siempre debemos tener como monimo un yield
def funcion_geneador_contador(word):
    for i in word:
        yield i, word.count(i)


print("*** Usando un generador ***")
print(dict(funcion_geneador_contador("humanidad")))
print(dict(funcion_geneador_contador("humano")))
