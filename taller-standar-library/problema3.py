"""
Escriba un programa de Python para listar todos los archivos en un directorio en Python.
(por precaución que sea en una carpeta temporal y 
que no contenga archivos importantes, coloque copias)
"""

import os

# Es obligatorio que listdir tenga una ruta? NO
# Si a listdir no le paso nada por defecto toma la carpeta donde estoy

#! Si una carpeta o archivo empieza con un "." significa
#! que esta oculta
for file in os.listdir():
    print(file)
