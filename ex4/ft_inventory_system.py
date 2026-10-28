from sys import argv


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for i in argv[1:]:
        parts = i.split(":", 1)
        if len(parts) != 2:
            print(f"Error - invalid parameter '{parts}'")
            continue
        name, qtd_str = parts
        if name in inventory:
            print(f"Redundant item {name} - discarding")
            continue
        try:
            qtd = int(qtd_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory[name] = qtd

    items_list = inventory.keys()
    total = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(items_list)}")
    print(f"Total quantity of the {len(items_list)} items: {total}")

    item_most_abundant: str = list(items_list)[0]
    item_least_abundant: str = list(items_list)[0]
    for name in inventory:
        qtd = inventory[name]
        if inventory[name] > inventory[item_most_abundant]:
            item_most_abundant = name
        if inventory[name] < inventory[item_least_abundant]:
            item_least_abundant = name
        percent = round(qtd / total * 100, 1)
        print(f"Item {name} represents: {percent}%")

    print(f"Item most abundant: {item_most_abundant} "
          f"with quantity {inventory[item_most_abundant]}")
    print(f"Item least abundant: {item_least_abundant} "
          f"with quantity {inventory[item_least_abundant]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
