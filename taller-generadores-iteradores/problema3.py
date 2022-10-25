# Dada la lista de
# notas[15, 20, 18] y la lista de
# alumnos["Marcelo", "José", "Juan"],
# imprimirlos de la siguiente forma:

# 1 -> Jose: 20
# 2 -> Juan: 18
# 3 -> Marcelo: 15

# No usar range, ni comparadores. Hint: usar sorted
notas = [15, 20, 18]
alumnos = ["Marcelo", "José", "Juan"]

# reminder
# print(sorted(notas, reverse=True))

alumnos_notas = sorted(list(zip(alumnos, notas)))
print(alumnos_notas)

for contador, (alumno, nota) in enumerate(alumnos_notas, start=1):
    print(contador, "->", alumno, ":", nota)
