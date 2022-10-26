"""
El presente ejercicio se enfoca en la manipulación de fechas utilizando datetime (Documentación oficial)

Explore la documentación y escriba un programa Python para mostrar la fecha y la hora actuales bajo los siguientes formatos de ejemplo (imaginando hoy fuese 10 de septiembre del 2022):

10-09-22 ✅
10-09-2022 ✅
Hoy día es Saturday ✅
10~09~2022 ✅
10-09-2022 14:20:51 ✅
En caso obtengan Hoy día es Sábado no habría problema alguno, no se evaluará lo referente a los idiomas.

Es importante mencionar que la exploración de la documentación es importante sobretodo cuando le toque explorar de un paquete que no sea popular
"""

from datetime import datetime

hoy = datetime.today()

print(hoy.strftime("%d-%m-%y"))
print(hoy.strftime("%d-%m-%Y"))
print("Hoy dia es", hoy.strftime("%A"))
print(hoy.strftime("%d~%m~%Y"))
print(hoy.strftime("%d-%m-%Y %H:%M:%S"))
