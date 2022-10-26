"""
Escriba un programa en Python que acepte el perímetro de un círculo que escriba un usuario.

Finalmente el programa debe imprimir:

El valor de π con 7 decimales.
El valor del área de dicho círculo (con 3 decimales) así como el valor del radio de dicho círculo (con 2 decimales).
Pistas

En geometría, el área encerrada por un círculo de radio r es π*r^2.
Del módulo math obtenga el valor de π para los cálculos que requiera.
La letra griega π representa una constante, que es igual a la relación entre la circunferencia de cualquier círculo y su diámetro.
"""

import math

# Nota: Como input de usuario tenemos el perimetro
perimetro = float(input("Ingrese el perimetro: "))
# PI
pi = round(math.pi, 7)
# RADIO
radio = round(perimetro / 2 * pi, 2)
# AREA
area = round(pi * radio ** 2, 3)

print("PI 7 decimales", pi)
print("Radio", radio)
print("Area ", area)
