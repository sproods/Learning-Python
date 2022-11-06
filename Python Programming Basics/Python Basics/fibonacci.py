# Programa que muestra en pantalla los primeros n números de la serie de Fibonacci, donde n es un número entero digitado por el usuario.
import sys

print('Digite el número de términos que la serie de Fibonacci que desea que se muestren en pantalla:')
n = int(input())

count = 1
while n < 0:
    print('Digite, por favor, un número positivo mayor que cero:');
    n = int(input())
    count += 1
    if count == 5:
        print('\nGame over...')
        sys.exit()

a, b = 0, 1
i = 0

while i < n:
    print(b, end = ', ')
    a, b = b, a + b
    i += 1