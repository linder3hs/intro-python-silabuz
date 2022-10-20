# Como es la sintaxys de una funcion
# def va a indicar que esto es una funcion
# nombre_function
# (parametros):
# def nombre_function():

# ** Recomendacion: El nombre de una funcion siempre deber un verbo infinitivo
# ** ar, er, ir ...

# creacion
def saludar_alumnos(nombre, apellido="Perez"):
    print(f"Bienvenido {nombre} {apellido} al bootcamp de backend")


# como uso esta funcion
# solo tenemos que llamarla por su nombre
# !! Nota: Recurden llenar los parametros solicitado por la funcion
saludo_1 = saludar_alumnos("Angel")
print(saludo_1)  # Esto es un None porque la funcion no retorna nada
saludar_alumnos("Isaac", "Zapata")
saludar_alumnos("Mijail")

saludar_alumnos(apellido="Hassinger", nombre="Linder")


# Esta funcion tiene la instruccion de elevar un numero al cubo
#! return indicar que es el final de la funcion, es decir lo que este debajo de el ya no se ejecuta
#! tambien podemos retornar nada
def calcularCubo(n):
    return n ** 3


def esPar(n):
    if n % 2 == 0:
        return "Es par"
    else:
        return


print("*** Usando return ****")
valor1 = esPar(10)
print(valor1)
valor2 = esPar(13)
print(valor2)
print("*** Usando return ****")


numero = calcularCubo(10)
numero2 = calcularCubo(8)
print(numero)
print(numero2)


def calcular_primer_puesto(nombre="Alumno", edad="", nota1=None, nota2=11, nota3=12):
    return f"El alumno {nombre} con edad {edad} tiene en promedio {(nota1 + nota2 + nota3) / 3}"


print(calcular_primer_puesto(nota2=10))
print(calcular_primer_puesto(nombre="Juan", nota1=18))

lista = [10, 20]

print(lista.append(15))
print(lista)
