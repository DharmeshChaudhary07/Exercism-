"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    count_dict = {}
    for item in items:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict



def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    count = 0
    for i in items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory
        
def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    # for i in items:
    #     if i in inventory:
    #         inventory[i] -= 1
    #         if inventory[i] <= 0:
    #             inventory.pop(i)     
    # return inventory
    
    for i in items:
        if i in inventory:
            inventory[i] = max(0, inventory[i] - 1)
    return inventory

    


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """
    result = []
    for item, count in inventory.items():
        if count > 0:
            result.append((item, count))
    return result

    # result = []
    # for i, count in inventory:
    #     if count > 0:
    #         result.append(i, count))
    # return result
    
    
