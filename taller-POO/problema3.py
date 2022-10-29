"""
Cree una clase Punto con los siguientes atributos: X, Y

Cree el método mostrar_punto, el cual imprime lo siguiente.

El punto está en ( "X", "Y" )
Luego realice la composición con la clase figura creada anteriormente.

Nota:

Utilice el método mostrar_punto dentro de mostrar_figura
Utilice los mismos datos del ejercicio anterior
Cree un objeto Figura y llame a mostrar_figura, luego elimine el objeto.
"""


class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_punto(self):
        print(f"El punto esta en {self.x}, {self.y}")


class Figura:

    def __init__(self, nombre, area, x, y):
        self.nombre = nombre
        self.__area = area
        self.x = x
        self.y = y
        self.punto = Punto(x, y)

    def __del__(self):
        print("Objeto Figura destruido")

    def get_area(self):
        return self.__area

    def set_area(self, area_nueva):
        self.__area = area_nueva

    def mostrar_figura(self):
        print(
            f"La figura se llama {self.nombre} \nTiene un área de {self.__area} m ^ 2 \nE inicia en las coordenadas({self.x}, {self.y})")
        print("-"*30)
        self.punto.mostrar_punto()


figura = Figura("Circulo", 30.5, -1, 2)
figura.mostrar_figura()
del figura
