"""
Instale la librería requests de Python.

Luego, de la API Rick and Morty API, use el siguiente link:

https://rickandmortyapi.com/api/character/1,2,3,4,5

Con dicho request, extraerá 5 personajes de la serie.

Cree una clase RickAndMortyCharacter que tenga los siguientes atributos.

Name
Status
Specie
Gender
La clase debe contar con el método saluda, la cual imprime lo siguiente:

Hola, soy "Name" y mis datos son los siguientes:
Estado: "Status"
Soy de la especie : "Specie
Y soy del género: "Gender"
Con el request realizado a la API, transforme la información a un json y convierta cada registro a un objeto de su clase creada, para luego ingresarlo en una lista.

Con la lista de objetos, recorrala y utilice "saluda" con cada objeto de la lista.
"""

import requests


class RickAndMortyCharacter:

    def __init__(self, name, status, specie, gender):
        self.name = name
        self.status = status
        self.specie = specie
        self.gender = gender

    def saludar(self):
        print(f"Hola, soy {self.name} y mis datos son los siguientes:",
              f"\nEstado: {self.status}",
              f"\nSoy de la especie: {self.specie}",
              f"\nY soy del género: {self.gender}",
              )


# Peticion
url_api = "https://rickandmortyapi.com/api/character/1,2,3,4,5"
response = requests.get(url_api)

data = response.json()

for character in data:
    rmcharacter = RickAndMortyCharacter(
        character["name"],
        character["status"],
        character["species"],
        character["gender"]
    )
    rmcharacter.saludar()
    print("-"*100)
