# Set
# Formar de declararse
# set tiene datos unicos
numeros = {1, 1, 1, 1, 3, 3, 4, 5, 6}
numeros2 = set([1, 1, 2, 3, 4, 5])
print(numeros)
print(numeros2)
numeros.add(1)
numeros.add(2)
print(f"numeros {numeros}")
numeros.remove(1)
print(f"numeros {numeros}")
numeros.discard(10)
# Diferencia entre remove y discard
# Si no se encuentra un valor a eliminar
# usando discard este simplemente lo ignora
# mientras si usamamos remove y este valor
# no existe lanza un error en consola
print(f"numeros {numeros}")

s1 = {2, 4, 5, 8}
s2 = {1, 2, 4, 9}
# Nota cuando usamos union, recordemos que
# set tiene datos unicos por enede no habra 
# repetidos
# Nota el orden de union no importa
print(f"Union 1 {s1.union(s2)}")
print(f"Union 2 {s2.union(s1)}")

print(f"Intersection 1 {s1.intersection(s2)}")

# Nota en este caso si debemos tener en cuenta
# que set ejecuta el difference
print(f"Difference 1 {s1.difference(s2)}")
print(f"Difference 2 {s2.difference(s1)}")
