"""
Cree la clase Circulo la cual herede de la clase Figura, 
adicione los siguientes atributos:

Radio
Centro X
Centro Y
Nota: Con centro "X" y "Y", agregue una composición con la clase Punto.

Cree el método mostrar_circulo, el cual haga uso de mostrar_figura, además agregue las siguientes impresiones:

El círculo tiene un radio de "Radio"
Centro:
El punto de inicio esta en ( "Centro X", "Centro Y" )
Nota:

Para el centro utilice mostrar_punto
Utilice los mismo datos del ejecicio 3 y adicione lo siguiente.
Radio = 3
Centro X = 2
Centro Y = 3
Cree un objeto circulo, llame a mostrar_circulo y luego elimine el objeto
"""
from problema3 import Figura, Punto


class Circulo(Figura):

    def __init__(self, radio, centro_x, centro_y, nombre, area, x, y):
        Figura.__init__(self, nombre, area, x, y)
        self.radio = radio
        self.centro = Punto(centro_x, centro_y)

    def __del__(self):
        Figura.__del__(self)

    def mostrar_circulo(self):
        self.mostrar_figura()
        print("-"*50)
        print(f"El círculo tiene un radio de {self.radio}")
        print("Centro:")
        self.centro.mostrar_punto()


circulo = Circulo(3, 2, 3, "Circulo", 30.5, -1, 2)
circulo.mostrar_circulo()


del circulo
