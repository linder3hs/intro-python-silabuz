"""
Del ejercicio 6, añada polimorfismo a la función heredada tipo_carro,
para eliminar los condicionales del número de asientos y directamente imprima:

Es un bus
Además de los datos de la llanta.
"""

from problema4 import Vehiculo


class Bus(Vehiculo):

    def __init__(self, tipo_uso, empresa, marca, anio, placa, num_asientos):
        Vehiculo.__init__(self, marca, anio, placa, num_asientos)
        self.tipo_uso = tipo_uso
        self.empresa = empresa

    def tipo_carro(self):
        print("Es un bus")
        self.rueda.mostrar_llanta()

    def mostrar_bus(self):
        self.mostrar_carro()
        self.tipo_carro()
        print(f"El autobus se usa para transporte {self.tipo_uso}")
        print(f"La empresa a la que pertenece es: {self.empresa}")


bus = Bus("escolar", "Empress", "Toyota", 2020, "ABC-416", 4)
bus.mostrar_bus()
