"""
Cree la clase Bus que herede de la clase Automovil y adicione los siguientes atributos:

Tipo de uso
Empresa
Cree el método "mostrar_bus", el cual haga uso de "mostrar_carro" y "tipo_carro" de la clase automovil, además agrege la siguiente impresión.

El autobus se usa para transporte "Tipo de uso"
La empresa a la que pertenece es: "Empresa"
Notas:

Use mostrar_carro y tipo_carro dentro de mostrar_bus

Use los datos del ejecicio 4 y adicione lo siguiente:

Tipo de uso = escolar
Empresa = Empress

"""
from problema2 import Vehiculo


class Bus(Vehiculo):

    def __init__(self, tipo_uso, empresa, marca, anio, placa, num_asientos):
        Vehiculo.__init__(self, marca, anio, placa, num_asientos)
        self.tipo_uso = tipo_uso
        self.empresa = empresa

    def mostrar_bus(self):
        self.mostrar_carro()
        self.tipo_carro()
        print(f"El autobus se usa para transporte {self.tipo_uso}")
        print(f"La empresa a la que pertenece es: {self.empresa}")


bus = Bus("escolar", "Empress", "Toyota", 2020, "ABC-416", 21)
bus.mostrar_bus()
