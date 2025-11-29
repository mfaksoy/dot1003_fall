#Task66
inventory = {
    "item1": 3,
    "item2": 1,
    "item3": 5
}

def add_item(item, quantity):
    inventory[item] = inventory.get(item, 0) + quantity 

def remove_item(item, quantity):
    if item not in inventory:
        return 

    remaining = inventory[item] - quantity
    if remaining <= 0:
        del inventory[item]
    else:
        inventory[item] = remaining

add_item("item1", 5) 
add_item("item4", 1) 

remove_item("item4", 6) 
remove_item("item1", 2) 

for key, value in inventory.items():
    print(f"{key}: {value}")