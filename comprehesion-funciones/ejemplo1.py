numeros = []

for i in range(1, 10):
    numeros.append(i ** 2 + i ** 3)

print(numeros)

print("*** Migrando a comprehesion ***")

numeros2 = [j ** 2 for j in range(1, 10) if j % 2 == 0]

print(numeros2)

print("***comprehesion con diccionarios ***")

edades = {f"key-{i}": i for i in range(10, 20)}
print(edades)

print("***comprehesion ejemplo nombres ***")
lista = ["Pepe", "Maria", None, "Luis", None]

# Nota si queremos usar un else podemos cambiar un
# la sintaxis y poner la condicion delante del for

nombres = [nombre.capitalize() for nombre in lista if nombre is not None]
nombres2 = [nombre.capitalize() if nombre is not None else "" for nombre in lista]

print(nombres)
print(nombres2)
