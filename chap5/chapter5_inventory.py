def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    # sorted inventory
    for k in sorted(inventory.keys()):
        print('{:>2} {:<15}'.format(str(inventory[k]), k))
        item_total += inventory[k]
    print('Total number of items: {:d}'.format(item_total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby',
    'ruby',
    'ruby',
    'iron sword']

stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
