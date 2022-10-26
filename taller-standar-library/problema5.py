"""
Escriba un programa en Python para calcular el número de
días entre dos fechas. No es necesario que use 
inputs para el ingreso de las fechas.
"""

"""
2022-10-26 - 2022-10-22 
Tenemos 4 dia de diferencia
"""
from datetime import datetime

fecha1 = datetime(2022, 10, 26)
fecha2 = datetime(2022, 10, 22)

diferencia = fecha1 - fecha2
# Nos pide calcular los dias
print("Diferencia de dias entre 2 fechas", diferencia.days)
