# Programa que imprime en pantalla una serie de formas piramidales utilizando el for statement.

num = int(input('Digite un número: '))

for i in range(num + 1):
    for j in range(i):
        print(j + 1, end = ' ')
    print('\n')