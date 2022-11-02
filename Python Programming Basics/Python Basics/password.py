password = 'magicWord'
a = 0

while True:
    print('Digite su contraseña:')
    yourPassword = input()

    if yourPassword != password:
        a += 1
        # continue          # Esta declaración hace que vuelva al inicio sin pasar por el último if.
    else:
        break

    if a == 5:
        break


if a < 5:
    print('\nAcceso concedido')
elif a == 5:
    print('\nAcceso denegado')