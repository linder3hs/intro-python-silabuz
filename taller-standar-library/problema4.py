"""
Sin usar bibliotecas como pandas.

Generar un archivo local con el contenido del siguiente archivo:

https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Utilizando import csv

Calcular:

El promedio de edad.
La distribución del sexo (número de mujeres vs varones).
El número de sobrevivientes y fallecidos.

"""
import csv

with open("titanic.csv", "r") as file:
    reader = csv.DictReader(file)
    # reader es iterable? SI

    # Promedio de edades
    edades = []
    # Numero de mujeres
    mujeres = []
    # Numero de varones
    varones = []
    # numero de sobrevivientes
    sobrevivientes = []
    # numero de fallecidos
    fallecidos = []

    for persona in reader:
        # Edades
        if persona["Age"] != "":
            edades.append(float(persona["Age"]))

        # Mujeres
        if persona["Sex"] == "female":
            mujeres.append(persona["Name"])
        else:
            varones.append(persona["Name"])

        if persona["Survived"] == "1":
            sobrevivientes.append(persona["Name"])
        else:
            fallecidos.append(persona["Name"])

    edades_promedio = sum(edades) / len(edades)
    cantidad_mujeres = len(mujeres)
    cantidad_varones = len(varones)
    cantidad_sobrevivientes = len(sobrevivientes)
    cantidad_fallecidos = len(fallecidos)

    res_file = open("resultado.txt", "w")
    res_file.writelines(
        f"Promedio de edades: {edades_promedio}" +
        f"\nCantidad de mujeres: {cantidad_mujeres}" +
        f"\nCantidad de varones: {cantidad_varones}" +
        f"\nCantidad de sobrevivientes: {cantidad_sobrevivientes}" +
        f"\nCantidad de fallecidos: {cantidad_fallecidos}"
    )

# r => read (leer)
# w => write (escribir)

# fileT = open("test.txt", "w")
# fileT.writelines(
#     "hola" +
#     "\ncomo estas"
# )
