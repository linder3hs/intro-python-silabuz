import random

# Quiero que un entero
number = random.randint(1, 1000)
print("trampa", number)

while True:
    num = int(input("Ingrese un numero: "))

    if num == number:
        print("Adivinaste el numero", num)
        break
    elif num < number:
        print("Debes ingresar un numero mayor")
    else:
        print("Debes ingresar un numero menor")
