stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print('  ' + str(v) + '\t ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

# main
print('Digite la opción de su preferencia:')
print('1. Añadir nuevos keys')
print('2. Aumentar los valores de keys existentes')
print('3. Disminuir los valores de keys existentes')
print('4. Ver el inventario total')
op = input()

if str(op) == '1':
    print(op)
elif str(op) == '4':
    displayInventory(stuff)
