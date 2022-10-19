num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

# Por default decimos es res = num2
# Message: Un problema siempre tiene mas de 1 solucion
res = num2

if num1 > num2:
    res = num1

print("El número mayor es: ", res)
