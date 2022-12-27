stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print('  ' + str(v) + '\t ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

# Función que realiza la adición de nuevos keys, o componentes, pero si ese componente existe modifica el valor
def newKey(inventory):
    print('Digite el nuevo key:')
    key = input()
    print('Ahora, digite el nuevo valor para ' + key + ':')
    value = input()
    inventory.setdefault(key, int(value))

# main
while True:
    print('Digite la opción de su preferencia:')
    print('1. Añadir nuevos keys')
    print('2. Aumentar los valores de keys existentes')
    print('3. Disminuir los valores de keys existentes')
    print('4. Ver el inventario total')
    op = input()

    if int(op) == 1:
        newKey(stuff)
    elif int(op) == 2:
        addValues(stuff)
    elif int(op) == 3:
        quitValues(stuff)
    elif int(op) == 4:
        displayInventory(stuff)

    print('Desea digitar otra opción? (s/n):')
    op2 = input()

    if op2 == 'n':
        print('Gracias por sus consultas!')
        break

