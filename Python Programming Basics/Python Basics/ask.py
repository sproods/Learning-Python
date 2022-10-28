# El programa recoge datos del usuario y los utiliza para imprimir con ellos en la pantalla del ordenador de manera que pueda alterar algunos resultados.

print('Hola!, \nDigita, por favor, tu nombre: ')
name = input()

print('Hola!', name, ', ¿te encuentras bien?')
estado = input();

if estado == 'sí' or 'si' or 'Sí' or 'Si' or 'SÍ':
    print('Me alegro muchísimo')
    print('Dime tu edad: ')
    edad = input()
    print('¿Ya celebraste tu cumpleaños este año?')
    res = input()
    if res == 'sí' or 'si' or 'Sí' or 'Si' or 'SÍ':
        año = 2022 - int(edad)
        if año >= 2000:
            print('Eso quiere decir que naciste en el', año, '.\nEres bastante joven!')
        elif año < 2000:
            print('Eso quiere decir que naciste en', año, '.\nYa eres todo un veterano!')
    elif res == 'no' or 'No' or 'NO':
        año = 2021 - int(edad)
        if año >= 2000:
            print('Eso quiere decir que naciste en el', año, '.\nEres bastante joven!')
        elif año < 2000:
            print('Eso quiere decir que naciste en', año, '.\nYa eres todo un veterano!')
elif estado == 'no' or 'No' or 'NO':
    print('Espero, sinceramente, que mejores tu estado. :)')
