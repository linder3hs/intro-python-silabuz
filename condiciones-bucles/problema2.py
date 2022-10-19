numbers = []  # lista vacia

while True:
    num = int(input("Ingresa un numero: "))

    if num == 0:
        print(f"La suma de los numeros es {sum(numbers)}")
        break

    numbers.append(num)
