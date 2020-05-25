# A program that has two functions: one which adds items and their count to an existing inventory, and one which
# prints out the items and their count from the inventory


def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        item_total += value
        print(value, key, sep=" ")
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
