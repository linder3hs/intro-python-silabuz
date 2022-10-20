# Usando argumentos
def multiplicando(*numeros):
    print(numeros)
    print("*" * 20)
    for numero in numeros:
        print(numero)
    print("*" * 20)


multiplicando()
multiplicando(1)
multiplicando(1, 2)
multiplicando(1, 2, 3)
multiplicando(1, 2, 3, 4)
multiplicando(1, 2, 3, 4, 5)
multiplicando(1, 2, 3, 4, 5, 6)


def calcular_area_triangulo(base, altura, nombre):
    print(nombre)
    print(base * altura / 2)


datos = [10, 20]
datos2 = [90, "Lucho"]
print(*datos)
calcular_area_triangulo(*datos, "Pepe")
calcular_area_triangulo(nombre="Juan", *datos)
# 5 => base
# 90 => altura
# lucho => nombre
calcular_area_triangulo(5, *datos2)
# Error por el orden de los argumentos
# calcular_area_triangulo(altura=10, *datos2)

message = "Hola-mundo"
print(message)
print(*message)

# Una funcion puede retornar mas de un valor


def lista_promedio_notas(notas1, notas2, notas3):
    return sum(notas1)/len(notas1), sum(notas2)/len(notas2), sum(notas3)/len(notas3)


notas_1 = [1, 2, 3, 4]
notas_2 = [10, 12, 23]
notas_3 = [10, 15, 18, 20, 21]

resultado = lista_promedio_notas(notas_1, notas_2, notas_3)
print(resultado[0])
print(resultado[1])
print(resultado[2])


# forma2
# x, y, z = 1, 2, 3
n1, n2, n3 = lista_promedio_notas(notas_1, notas_2, notas_3)

print(n1, n2, n3)
