# Diccionaros
# Elemntos key => value
# clave => valor
phone = 'phone_number'
user = {
  'name': 'Linder',
  'last_name': 'Hassinger',
  1: 'aa',
  1.2: 'ASDAS',
  phone: 999999,
  # colorca un diccionario dentro de un diccionario
  'user2': {
    'name': 'Pepe'
  }
}
print(user['name'])
print(user['user2'])
print("*"*30)

listKeys = list(user.keys())
print("lista")
print(listKeys[1])
print("lista")

print(user)
print(user.keys()) #imprime los keys
print(user.values()) #imprimer los valores
print(user.items()) # imprime los items

# Objeto => Podemos decir que es un diccionario
# Podemos tener un array de diccionarios?

print("***** Users ******")
# Podemos decirle de estas formas
# array de objetos # algo generico
# lista de objetos
# lista de diccionarios # en el mundo de python
# array de diccionarios
users = [
  {
    'name': 'User1',
    'last_name': 'Lastname1'
  }, 
  {
    'name': 'User2',
    'last_name': 'Lastname2'
  }, 
  {
    'name': 'User3',
    'last_name': 'Lastname3'
  }
]
