"""
Añada polimorfismo a mostrar_figura, para que imprima lo siguiente.

Es un círculo y tiene un área de: "Area"
Pista: Recuerdar que en el Problema 1 se creó un getter para área y 
que al usar herencia, tanto métodos como atributos no privados se pueden 
utilizar dentro de la clase que hereda.
"""

from problema1 import Figura


class Circulo(Figura):

    def __init__(self, radio, centro_x, centro_y, nombre, area, x, y):
        Figura.__init__(self, nombre, area, x, y)
        self.radio = radio
        self.centro_x = centro_x
        self.centro_y = centro_y

    def mostrar_figura(self):
        print(f"Es un círculo y tiene un área de: {self.get_area()}")


circulo = Circulo(3, 2, 5, "Circulo", 30.5, -1, 2)
circulo.mostrar_figura()
