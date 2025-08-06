from game_rooms import all_rooms
from game_items import all_items
from game_items import all_keys
from game_items import player_inventory
from game_items import player_keys

def remove_room_item(item_taken, current_room, rooms_list = all_rooms) -> list:
    room_items = rooms_list.get(current_room).get('items')
    room_items.remove(item_taken)
    return room_items

def print_inventory_add(new_item, inventory = player_inventory):
    if inventory_full(inventory):
        print("Your inventory is full. You cannot carry any more items.")
    elif not inventory_full(inventory):
        inventory_add(new_item, inventory)
        print(f"You pick up the {new_item}")
    else:
        print("Debug: problem with print_inventory_add()")

def inventory_add(new_item, inventory = player_inventory):
    """Adds the specified item to the player's inventory
    after first checking if there is space"""
    if inventory_full(inventory):
        return inventory
    inventory.append(new_item)
    return inventory

def inventory_full(inventory = player_inventory) -> bool:
    """Helper function to check if your inventory is full
    before adding items. Returns True if full and False if there is space"""
    if not isinstance(inventory, list):
        raise TypeError("Non list supplied to inventory_full()")
    if len(inventory) >= 8:
        return True
    return False

def standardise_text(text) -> str:
    """Standardises text by removing spaces and converting to lower case
    to make comparisons/lookups easier"""
    if not isinstance(text, str):
        raise TypeError("value provided to standardise_text() was not a string")
    text = text.lower().replace(" ", "")
    return text

def enter_room(current_room, new_room, rooms = all_rooms, keys = player_keys) -> str:
    # You need new variables to preserve the label formats for printing
    current_room_flat = standardise_text(current_room)
    new_room_flat = standardise_text(new_room)
    if new_room_flat == "outside":
        if rooms.get('outside').get('trigger_special'):
            print(rooms.get('outside').get('desc_special'))
            rooms.get('outside').update(trigger_special = False)
            return current_room_flat
        elif not rooms.get('outside').get('trigger_special'):
            print(rooms.get('outside').get('desc'))
            return current_room_flat
    # Check the proposed room can be entered from where the player's current room
    if new_room_flat not in rooms[current_room_flat]["access"]:
        print(f"\nYou cannot enter the {new_room} from {current_room}.")
        return current_room_flat
    # check the player doesn't need a key or lockpick
    if rooms[new_room_flat]['locked'] is not None:
        if rooms[new_room_flat]['locked'] not in keys:
            needed_key = rooms[new_room_flat]['locked']
            print(f"\nYou need the {needed_key} to enter the {new_room}.")
            return current_room_flat
        # unlock if they have the needed key
        elif rooms[new_room_flat]['locked'] in keys:
            print(f"\nYou unlocked the {new_room}.")
            rooms[new_room_flat].update(locked = None)
            return new_room_flat
    return new_room_flat

def explore_room(current_room, rooms = all_rooms):
    current_room = standardise_text(current_room)
    print_room = rooms.get(current_room).get('label')
    print(f"\nYou are in the {print_room}")
    print(rooms.get(current_room).get('desc'))
    if rooms.get(current_room).get('items') is None or rooms.get(current_room).get('items') == []:
        print("You do not find any items of interest.")
    else:
        print("\nYou search the room and find the following items:")
        for item in rooms.get(current_room).get('items'):
            print(f"- {item}")

def status_room(current_room, rooms = all_rooms):
    current_room = standardise_text(current_room)
    print_room = rooms[current_room]['label']
    print(f"\nYou are currently in the {print_room}")
    print("From here, you can go to:")
    for room in rooms.get(current_room).get('access'):
        next_room = rooms.get(room).get('label')
        print(f"- {next_room}")

def status_inventory(inventory = player_inventory, keys = player_keys,
                        item_list = all_items, key_list = all_keys):
    # check if the list is empty:
    if not player_inventory:
        print("\nYou are not carrying anything")
    else:
        print("\nYou have the following in your inventory:")
        for item in player_inventory:
            print_item_label = all_items.get(item).get('label')
            print_item_desc  = all_items.get(item).get('desc')
            print(f"- {print_item_label}: {print_item_desc}")
    print("\nYou have the following keys:")
    for key in player_keys:
        key_label = key_list.get(key).get('label')
        key_desc = key_list.get(key).get('desc')
        print(f"- {key_label}: {key_desc}")


def print_help():
    print("""
    e - (e)xplore room        w - check (w)eapon
    g - (g)o to room
    h - (h)elp (this page)
    i - check (i)nventory
    p - (p)ickup item
    q - (q)uit to terminal
    m - (m)ap""")
