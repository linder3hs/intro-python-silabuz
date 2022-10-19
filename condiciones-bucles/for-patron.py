print("Solucion 1:")

for i in range(1, 6):
    print(i * "*")

for j in range(4, 0, -1):
    print(j * "*")

print("Solucion 2:")

for index in range(1, 10):
    if index < 6:
        print(index * "*")
    else:
        print((10 - index) * "*")
