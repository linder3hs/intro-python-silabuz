invitados = []

while True:
    nombre = input("Ingrese su nombre: ")
    trajo_regalo = input("Trajo regalo? S/N: ")

    if trajo_regalo.upper() == "S":
        trajo_regalo = True
    else:
        trajo_regalo = False

    invitados.append({
        'nombre': nombre,
        'trajo_regalo': trajo_regalo
    })

    acabar = input("Deseas acabar y lista los invitados con regalo? S/N: ")

    if acabar.upper() == "S":
        print("Invitados buena onda que si traen regalos. !!!")
        for invitado in invitados:
            if invitado['trajo_regalo']:
                print(invitado['nombre'])
        break
