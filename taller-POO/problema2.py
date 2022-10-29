"""
Cree una clase Automovil con los siguientes atributos.

Marca
Año
Placa
Número de Asientos
Escriba los getters y setter del atributo marca.

Cree dos métodos, mostrar_carro y tipo_carro.

mostrar_carro imprime:

El carro es de marca "Marca" del año "Año"
Y tiene placa número "Placa"


tipo_carro imprime:

Si el número de asientos es mayor a 20, imprimir:

El automóvil es un bus.
Si el número de asientos es mayor a 10, imprimir:

El automóvil es una combi.
Si no, imprimir:

El automóvil es un carro normal
Crear un objeto con los siguientes datos, y llamar a los métodos creados.

Marca = Suzuki
Año = 2010
Placa = ABC-456
Número de Asientos = 4
"""


class Vehiculo:

    def __init__(self, marca, anio, placa, num_asientos):
        self.__marca = marca
        self.anio = anio
        self.placa = placa
        self.num_asientos = num_asientos

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca_nueva):
        self.__marca = marca_nueva

    def mostrar_carro(self):
        print(f"El vehiculo es de marca {self.__marca} del año {self.anio}")
        print(f"Y tiene placa número {self.placa}")

    def tipo_carro(self):
        message = "El vehiculo es un carro normal."
        if self.num_asientos > 20:
            message = "El vehiculo es un bus."
        elif self.num_asientos > 10:
            message = "El vehiculo es una combi."

        print(message)

    def __del__(self):
        print("Objeto vehiculo destruido")


# vehiculo = Vehiculo("Suzuki", 2010, "ABC-456", 4)
# vehiculo.mostrar_carro()
# vehiculo.tipo_carro()

# del vehiculo
