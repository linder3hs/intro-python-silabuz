def deco1(funcion_parametro):
    def funcion_interna():
        print("Hola, estoy decorando esta función.")
        funcion_parametro()
        print("Terminé de decorar")
    return funcion_interna


@deco1
def mostrar() -> None:
    n: str = input("Ingrese un numero: ")
    print("Ingresaste el número", n)


print(mostrar())
