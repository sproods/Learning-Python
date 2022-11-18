# Programa que elige, entre los items de una lista cuyos elementos han sido digitados por el usuario, un elemento al azar.

import random

lista = []

while True:
    print('Digite el item ' + str(len(lista) + 1) + ' -(o solo presiona enter para terminar)-:');
    item = input()

    if item == '':
        break

    lista = lista + [item]

while True:
    randomIndex = random.randint(0, (len(lista) - 1))
    randomItem = lista[randomIndex]

    print('La opción, elegida al azar, es:')
    print(randomItem)

    print('\n¿Desea obtener otra opción aletoria? -1.si   0.no-')
    res = input()

    if res == '0':
        break

print('¡Gracias!')