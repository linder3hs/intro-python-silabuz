# Teniéndos los siguientes criterios:

# Desaprobado: nota < 11
# Destacado: nota > 16
# Aprobado: para el resto de casos

# Implementar registrar_aprobados como generador y
# que su único parametro de entrada sea alumnos_notas
# Posteriormente utilizar un bucle y enumerate para obtener la siguiente salida.

# 1 -> Marcelo: 15 (Aprobado)
# 2 -> Jose: 20 (Destacado)
# 3 -> Juan: 18 (Destacado)
# 4 -> Marco: 11 (Aprobado)
# 5 -> María: 4 (Desaprobado)
# 6 -> Ricardo: 7 (Desaprobado)
# 7 -> Liz: 14 (Aprobado)
# 8 -> Diego: 13 (Aprobado)
# 9 -> Roberto: 1 (Desaprobado)
# 10 -> Martin: 9 (Desaprobado)
# 11 -> Álvaro: 10 (Desaprobado)


notas = [15, 20, 18, 11, 4, 7, 14, 13, 1, 9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María",
           "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]

alumnos_notas = zip(alumnos, notas)


def registrar_aprobados(alumnos_notas):
    for (alumno, nota) in alumnos_notas:
        if nota < 11:
            yield alumno, nota,  "Desaprobado"
        elif nota > 16:
            yield alumno, nota, "Destacado"
        else:
            yield alumno, nota, "Aprobado"


for count, (nombre, nota, texto) in enumerate(registrar_aprobados(alumnos_notas), start=1):
    print(count, "->", nombre, ":", nota, f"({texto})")
