# Listas en python

# Formas de declarar una lista
nombres = ['Juan', 'Maria', 'Luisa', 'Luis']
print(nombres)
# cursos = list('React Python PHP') # ['React', 'Python', 'PHP']
cursos = list({'React', 'Python', 'PHP'})
print(cursos)
# anidacion de lista esto puede ser infinity
tiposDeDatos = [1, True, ['Pepe', 'Juana', ['React', 'PHP', 'DJango']]]
print(tiposDeDatos)

numeros = [1, 3, 2, 4, 5]  # 1,2,3,4,5 1,3,2,4,5
print(numeros)

# Quiero obtener el ultimo datos de la lista de numeros y nosotros no sabemos
# la cantidad de elementos
print(numeros[len(numeros) - 1])
# Pero si en python queremos contar al revez podemos usar numeros negativos
# y en ese caso empezamos desde el -1
print(numeros[-1])  # el ultumos elemento de mi lista
# print(numeros[-10]) # Si el elemento lanza el error list index out of range (fuera de rango)

# Usando rangos
print("*"*30)
# Si dice 3 en truco de indices restarle 1
cursos2 = ['Python', 'Anaconda', 'Flask', 'DJango']
print(cursos2[0:3])

# Lista inmutable
nombreDeCurso = "Curso de Pyhton"
print(nombreDeCurso[0])
# Slicing
# cuando aplicamos esto a un string los espacios tambien se cuentan
print(nombreDeCurso[5:8])
# Es poder reempalzar el elemento es la posicion 3 por PHP
cursos2[3] = 'PHP'
# Esto existe? No por ende no puede ser reemplazada
# cursos2[4] = 'DJango'
print(cursos2)

# Dir sirve para poder lista todas la funcion que tenga un tipo
# print(dir(cursos2))

# Count (esto va a contar la cantidad de veces que existe un elemento es lista)
# Nota: Si un elemento no existe en la lista e intentamos contarlo
# el resultado será 0, no se rompera nada
alumnos = ['Gerson', 'Carlos', 'Bill', 'Gerson', 'Bill', 'Juan']
# Es sensible a mayusculas o minusculas? Si
print(alumnos.count('Gerson'))

# Es posible el poder juntar 2 listas?
# Estamos añadiento los elemenots de cursos2 a alumnos
alumnos.extend(cursos2)
print(alumnos)

# Append es para agregar un elemento
# porque append lo colocal en la ultima posicion
cursos2.append("JavaScript")
print(cursos2)

# Index retorna la posicion de un elemento
# 4 porque es la posicion donde encontro este valor
print(cursos2.index('JavaScript'))
# Nota: Si un elemento se repite en la lista esto nos retorna el primero que encuentre
print(alumnos.index("Gerson"))

# Insert: Inserta un elemento en la lista pero cuando usamos esta funcion, podemos indicar
# la posicion que queremos usar, esto no va a reeemplazar al elemento existente, lo que
# hacer es mover el emento a la derecha
# Resumento el no reemmplaza, el desplaza
cursos2.insert(0, 'Ruby on Rails')
print(cursos2[0])
print(cursos2[1])

# Como borrar un elemento de una lista
# Para ellos existe la funcion pop si solo usamos esta esta eliminar el ultimo elemento
cursos2.pop()
print(cursos2)
# Ahora pop tambien puede recibir un indice ejemplo
# cursos2.pop(10) # Esto falla? Si porque no existe el elemento 10
print(cursos2)
alumnos.clear()  # Esto deja vacio a mi lista
print(f"alumnos => {alumnos}")  # Deja la lista vacia

# Sorted: Esta funcion ordena los elementos de una lista ejempl
numeros2 = [1, 100, 12, 3, 26, 1]
print(f"Sorted numeros2 {sorted(numeros2)}")
# Creen este funcion para textos (str)
nombres3 = ['Pepe', 'Andy', 'Pablo', 'Beca', 'Juan']
# La forma larga
nombres3 = sorted(nombres3)  # reverse = False
# Esta forma es la mas elegante
# Nota si tenemos duda siempre es bueno revisar el doc de la funcion
# llamando a reverse podemos colocar True
nombresDesc = sorted(nombres3, reverse=True)
print(f"Sorted nombres3 {nombres3}")
print(f"Sorted nombres3 {nombres3[::-1]}")
print(f"Sorted nombres3 {nombresDesc}")

print("in ")
nombres4 = ['Pepe', 'Maria', 'Sultano', 'Mengano']
print('Pepe' in nombres4) # IN => TRUE or FALSE
print('pepe' in nombres4)
