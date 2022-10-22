from typing import List, Any, Set, Dict

number: int = 10

number_2: int = 20
print(number)
print(number_2)


def saludo(nombre):
    return f"Hola mi nombre es {nombre}"


def saludar(nombre: str) -> str:
    return f"Hola mi nombre es {nombre}"


print(saludar("Juan"))

# creando un dict donde indicamos que el key => str value => str
nombres_2: dict[str: str] = {"nombre1": "Lucia", "nombre2": "Luis"}

estados: dict[int: str] = {
    1: "inicio",
    2: "en_progreso",
    3: "terminado",
    4: "eliminado"
}

# estados_2 = {
#     1: "inicio",
#     2: "en_progreso",
#     3: "terminado",
#     4: "eliminado",
#     "mi_aportacion": 1
# }

print(type(estados))

lista_bool: list[bool] = [True, False, False, 1]
print(lista_bool)
print(type(lista_bool))
