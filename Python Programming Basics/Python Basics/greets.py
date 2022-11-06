# Programa que muestra en pantalla tres frases dependiendo del dígito que se teclee.

print('Digite un número, especialmente si es uno o dos:')
spam = input()

if spam == '1':
    print('\nHello\n')
elif spam == '2':
    print('\nHowdy\n')
else:
    print('\nGreetings!\n')