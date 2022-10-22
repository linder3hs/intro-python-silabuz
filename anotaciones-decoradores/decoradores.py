# para hacer este cambio estamos modificando la estructura de
# nuesta funcion
def division(divisor, dividendo):
    return divisor/dividendo


# Aca estamos guarado la funcion division dentro de div
# por ende ahora div es una funcion
div = division
print(type(div))


def funcion_validacion(funcion_paremetro):
    # que es funcion_paremetro == div
    number = int(input("Ingresa un numero divisor: "))
    if number == 0:
        print("No es posible dividir por 0")
        # return: retornava un valor y rompia la funcion
        return
    print(funcion_paremetro(12, number))


funcion_validacion(div)


# print(division(12, 0))
# print(div(12, 4))

# Vamos a crar una funcion decoradora completa

# Siempre recibo una funcion como paramtro? Si
def funcion_decoradora(funcion_parametro):
    # Proposito de la funcion interna
    # Tiene como proposito ejecutar algo antes o despues de la
    # funcion_parametro
    # Ejemplo: quiero hacer una validacion antes de la funcion parametro
    # lo hacemos en la funcion interna
    # Genera que la funcion parametro mantenga su estructura y no se modifique
    def funcion_interna():
        # queremos ejecutar algo antes de esta funcion
        print("Esto se ejecuta antes de la funcion_parametro")
        funcion_parametro()
        print("Esto se ejecuta despues de la funcion_parametro")

    return funcion_interna


@funcion_decoradora
def funcion_prueba():
    print("Esta es la funcion que enviamos al decorador")


@funcion_decoradora
def funcion_prueba2():
    print("Esta es la segunda prueba")


print("======Prueba1=====")
funcion_prueba()
print("======Prueba2=====")
funcion_prueba2()
