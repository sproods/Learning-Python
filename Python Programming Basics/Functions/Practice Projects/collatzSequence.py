
# Función de Collatz.
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

# Programa principal.
print('Digite un número entero, por favor:')
N = int(input())

print('\nSECUENCIA DE COLLATZ:\n')

print(N)
while True:
    ans = collatz(N)
    print(ans)

    if ans == 1:
        break

    N = collatz(N)          # la variable 'N' ahora toma el valor obtenido de 'collatz(N)'.