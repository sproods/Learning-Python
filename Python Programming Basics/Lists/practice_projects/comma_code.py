# Proyecto de práctica.
# Programa que muestra en pantalla el contenido de una lista desplegada entre comas y la palabra 'and' para denotar la última palabra.

lista = []          # lista vacía

i = 0
while True:
    print('Digite la palabra ' + str(i + 1) + ':')
    word = input()
    
    if word != '':
        lista += [word]
        i += 1
    else:
        break

# función que mostrará en pantalla la lista
def catalogo(list_name):
    tam = len(list_name)
    
    for i in range(tam - 1):
        print(list_name[i], end=', ')
    
    print('and')
    print(list_name[-1])
    
# llamada a la función catalogo
catalogo(lista)