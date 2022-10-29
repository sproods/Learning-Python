# Programa que realiza un pequeño juego de cálculo con sumas y restas de cifras muy simples y predeterminadas.
# Además pide al usuario algunos datos que se almacenan en unos variables para poder interactuar de manera más efectiva.

print('Hola, me podría decir su nombre, por favor: ')
res = input()
if res == 'sí' or res == 'si':
    count = 0
    print('Digite su nombre, por favor: ')
    name = input()
    print('Hola,', name, '\b, gusto en conocerte. ¿Eres capás de resolver las siguientes tres operaciones aritméticas?:\n')

    # Primera prueba
    print('¿Cuánto es 23 + 19?: ')
    sol = input()
    if sol == '42':
        print('¡Respuesta correcta!\n')
        count += 1
    else:
        print('Esa no es la respuesta.\n')

    # Segunda prueba
    a = 3; b = 12; c = 9; d = (a * b) - c
    print('¿Cuál es el resultado de la siguiente operación aritmética?')
    print('(' + str(a) + ' x ' + str(b) + ') - ' + str(c))
    sol = input()
    if int(sol) == d:
        print('¡Respuesta correcta,', name, '\b!\n')
        count += 1
    else:
        print("Esa no es la respuesta.\n")

    # Tercera prueba
    print('Por último, ¿cuál es el residuo de la siguiente división?:')
    print('15 / 4:')
    sol = input()
    if int(sol) == 15 % 4:
        print('¡Respuesta correcta!\n')
        count += 1
    else:
        print('Esa no es la respuesta', name, '\n')

    # Celebración si se consiguió un puntaje perfecto
    if count == 3:
        print('¡Felicidades,', name, '\b, conseguiste un puntaje perfecto!')
    else:
        print('¡Sigue mejorando, vas por buen camino!\n')

else:
    print('Bueno, que tenga un buen día.\nYa volveré preguntar cuando esté de buen humor.')