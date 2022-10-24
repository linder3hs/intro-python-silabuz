def funcion_decoradora(function_parametro):
    def funcion_interna(number):   
        res = function_parametro(number)
        if res:
            print("Es par")
        else:
            print("Es impar")
    return funcion_interna


@funcion_decoradora
def calc_par_impar(n: int) -> bool:
    return n % 2 == 0


number = int(input("Ingrese un numero: "))
calc_par_impar(number)
