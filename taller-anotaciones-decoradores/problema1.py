# Implementar la función get_avg que calcule el promedio
# de una lista de números:

def funcion_decoradora(function_parametro):
    def funcion_interna(numbers):
        print("Inicio del cálculo del promedio de la lista de números.")
        print(function_parametro(numbers))
        print("El cálculo ha finalizado.")
    return funcion_interna


@funcion_decoradora
def get_avg(numbers: list) -> float:
    return sum(numbers) / len(numbers)


list_numbers = [10, 20, 21, 11, 12]
get_avg(list_numbers)
