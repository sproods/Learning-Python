password = 'magicWord'
a = 0

while True:
    print('Digite su contraseña:')
    yourPassword = input()

    if yourPassword != password:
        a += 1
    else:
        break

    if a == 5:
        break


if a < 5:
    print('\nAcceso concedido')
elif a == 5:
    print('\nAcceso denegado')