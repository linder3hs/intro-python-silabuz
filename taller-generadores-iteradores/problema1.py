# Dada la lista de
# notas[15, 20, 18] y la lista de
#  alumnos["Marcelo", "José", "Juan"] Imprimirlos de la siguiente forma:

notas = [15, 20, 18]
alumnos = ["Marcelo", "José", "Juan"]

for i in range(len(notas)):
    print(alumnos[i], ":", notas[i])

print("*** Usando ZIP ****")

for key, value in zip(alumnos, notas):
    print(key, ":", value)
