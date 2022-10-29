"""
Cree la clase Rueda con los siguientes atributos:

Marca = Michelin
Índice de carga = 16
Diámetro = 99
Cree el método mostrar_llanta, que imprima lo siguiente:

La llanta es de marca "Marca"
El índice de carga es de "Índice de carga"
Y tiene un diámetro de "Diámetro"
Realice la composición con la clase Automovil.

Notas:

Utilice mostrar_llanta dentro del método tipo_carro
Utilice los datos del Problema 2
Cree un objeto automovil, use mostrar_llanta y luego elimine el objeto
"""


class Rueda:

    def __init__(self, marca, indice_carga, diametro):
        self.marca = marca
        self.indice_carga = indice_carga
        self.diametro = diametro

    def mostrar_llanta(self):
        print(f"La llanta es de marca {self.marca}")
        print(f"El índice de carga es de {self.indice_carga}")
        print(f"Y tiene un diámetro de {self.diametro}")


class Vehiculo:

    def __init__(self, marca, anio, placa, num_asientos):
        self.__marca = marca
        self.anio = anio
        self.placa = placa
        self.num_asientos = num_asientos
        self.rueda = Rueda("Michelin", 16, 99)

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
        print("-"*50)
        self.rueda.mostrar_llanta()

    def __del__(self):
        print("Objeto vehiculo destruido")


vehiculo = Vehiculo("Suzuki", 2010, "ABC-456", 4)
vehiculo.mostrar_carro()
vehiculo.tipo_carro()

del vehiculo
