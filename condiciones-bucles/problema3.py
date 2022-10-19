numerosPosi = []
numerosNega = []

while True:
    num = int(input("Ingrese un numero: "))

    if (num == 0):
        print("La suma de posi: ", sum(numerosPosi))
        print("La suma de nega: ", sum(numerosNega))
        print("La cantidad de # ingresados es",
              len(numerosPosi) + len(numerosNega))
        break

    if num > 0:
        numerosPosi.append(num)
    else:
        numerosNega.append(num)
