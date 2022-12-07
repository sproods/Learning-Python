# Proyecto de práctica.
# Programa que muestra en pantalla el contenido de una lista desplegada entre comas y la palabra 'and' para denotar la última palabra.

# función que mostrará en pantalla la lista
def catalogo(list_name):
    tam = len(list_name)
    
    for i in range(tam - 2):
        print(list_name[i], end=', ')
    
    print(list_name[tam - 2] + ' and ' + list_name[tam - 1])
    
# Programa principal
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
    
# llamada a la función catalogo
catalogo(lista)