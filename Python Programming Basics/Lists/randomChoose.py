# Programa que elige, entre los items de una lista cuyos elementos han sido digitados por el usuario, un elemento al azar.

import random

lista = []

while True:
    print('Digite el item ' + str(len(lista) + 1) + ' -(o solo presiona enter para terminar)-:');
    item = input()

    if item == '':
        break

    lista = lista + [item]

randomIndex = random.randint(1, (len(lista) - 1))

randomItem = lista[randomIndex]

print(randomItem)