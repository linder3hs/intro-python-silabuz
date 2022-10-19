numeros = [1, 2, 3, 4, 5]

# recordemos que i es solo un nombre de variable
for i in numeros:
    if i % 2 == 0:
        print("Par", i)
    else:
        print("Impar", i)


nombre = "juanito perez"

for n in nombre:
    print(n)

print("**** Range *****")
# 0 ... 9
for j in range(10):
    print(j)

print("**** Range(inicio, final) *****")

# 10 ... 50
for index in range(10, 51):
    print(index)

print("**** Range(inicio, final, pasos) *****")

# 100 ... 1 de 5 en 5
# Si tenemos in error en definir el inicio y el fin
# esto no va a cashear nuestra app solo no hace nada
for num in range(100, 0, -5):
    print(num)

# Que el usuario ingrese un numero
# y en consola se vea la table de multiplicar

# 5
# 1 x 5 = 5
# 2 x 5 = 10
# .
# .
# .
# 12 x 5 = 60
