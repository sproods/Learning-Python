# El programa realiza un ordenamiento simple de tres o cuatro números.

print('Digite un número:')
a = input()
print('Digite un segundo número:')
b = input()
print('Digite un tercer número:')
c = input()

print('\n')
if a > b:
    if a > c:
        if b > c:
            print('El orden de los números es:', a, '\b,', b, '\b,', c)
        else:
            print('El orden de los números es:', a, '\b,', c, '\b,', b)
    else:
        print('El orden de los números es:', c, '\b,', a, '\b,', b)
elif b > c:
    if c > a:
        print('El orden de los números es:', b, '\b,', c, '\b,', a)
    else:
        print('El orden de los números es:', b, '\b,', a, '\b,', c)
else:
    print('El orden de los números es:', c, '\b,', b, '\b,', a)
