"""
Cree una clase figura, que tenga los siguientes atributos.

Nombre
Área
Coordenada X
Coordenada Y
Escriba sus respectivos getters y setters de área.

Y cree el método mostrar_figura, qué imprima lo siguiente:

La figura se llama "Nombre"
Tiene un área de "Área" m^2
E inicia en las coordenadas ( "X", "Y" )
Luego, cree un objeto con los siguiente datos.

Nombre = Círculo
Área = 30.5
Coordenada X = -1
Coordenada Y = 2
Llame al método mostrar_figura, y luego destruya el objeto.
"""


class Figura:

    def __init__(self, nombre, area, x, y):
        self.nombre = nombre
        self.__area = area
        self.x = x
        self.y = y

    def __del__(self):
        print("Objeto Figura destruido")

    def get_area(self):
        return self.__area

    def set_area(self, area_nueva):
        self.__area = area_nueva

    def mostrar_figura(self):
        print(
            f"La figura se llama {self.nombre} \nTiene un área de {self.__area} m ^ 2 \nE inicia en las coordenadas({self.x}, {self.y})")


# Como uso (instancio) a mi clase Figura
# figura = Figura("Circulo", 30.5, -1, 2)
# figura.mostrar_figura()
# del figura
