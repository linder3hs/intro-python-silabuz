"""
Obtenemos prácticas en una laboratorio de 
una universidad y nos solicitan implementar 
de un paper la siguiente expresión matemática:
"""

import math


def calcular_expresion(n1, n2, n3):
    e = math.e
    log = math.log
    cos = math.cos

    return (e ** (n1 + n2)) * (log(n3) / cos(n1))


print(calcular_expresion(1, 2, 3))
