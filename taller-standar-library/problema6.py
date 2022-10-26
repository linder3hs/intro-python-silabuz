"""
Crear el archivo ejemplo.csv copiando el contenido del siguiente archivo: https://pastebin.com/gumjjcpx

Desarrolle un función que lea el archivo y que de la columna
QuotaAmount, calcule el promedio de los valores para luego retornarlo.
"""

import csv


def calcular_promedio(file_name):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        valores = [float(person["QuotaAmount"]) for person in reader]
        return sum(valores) / len(valores)


print(calcular_promedio("ejemplo.csv"))
