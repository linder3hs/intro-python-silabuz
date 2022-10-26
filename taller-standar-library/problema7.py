"""
Del ejercicio anterior cree dos pruebas unitarias (use unittest),
una que compare el valor de retorno con "146633.33" y el otro con "15000",
ambos test deben dar "Ok" como salida.

Recuerde usar la palabra "test" al inicio de cada función con su prueba.
"""
from select import select
import unittest
# podemos importar una funcion de otro archivo?
# problema6 => El archivo donde estan mis funciones
# calcular_promedio => Es la funcion que retorna el promedio
from problema6 import calcular_promedio


class test_calcular_promedio(unittest.TestCase):

    def testUniSuccess(self):
        promedio = calcular_promedio("ejemplo.csv")
        self.assertAlmostEqual(promedio, 146633.33333333334)

    def testUnitError(self):
        promedio = calcular_promedio("ejemplo.csv")
        self.assertNotAlmostEqual(promedio, 15000)
