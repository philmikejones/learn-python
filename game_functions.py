from game_rooms import rooms

def standardise_text(text):
    """Standardises text by removing spaces and converting to lower case
    to make comparisons/lookups easier"""
    text = text.lower().replace(" ", "")
    return text

def enter_room(current_room, new_room):
    global rooms
    # You need new variables to preserve the label formats for printing
    current_room_flat = standardise_text(current_room)
    new_room_flat = standardise_text(new_room)
    # Check the proposed room can be entered from where the player's current room
    if new_room_flat not in rooms[current_room_flat]["access"]:
        print(f"\nYou cannot enter the {new_room} from {current_room}.")
        return current_room
    return new_room

def explore_room(current_room, first_entry = False):
    global rooms
    current_room = standardise_text(current_room)
    print_room = rooms.get(current_room).get('label')
    print(f"\nYou are in the {print_room}")
    if rooms.get(current_room).get('first_entry'):
        print(rooms.get(current_room).get('special_description'))
        rooms.get(current_room).update({'trigger_special' : False})
        return
    print(rooms.get(current_room).get('description'))
    if rooms.get(current_room).get('items') == None:
        print("You do not find any items of interest.")
    else:
        print("\nYou search the room and find the following items:")
        for item in rooms.get(current_room).get('items'):
            print(f"- {item}")

def status_room(current_room):
    global rooms
    # standardise string for easier lookup
    current_room = standardise_text(current_room)
    print_room = rooms[current_room]['label']
    print(f"\nYou are currently in the {print_room}")
    print(f"debug current_room: {current_room}")
    print("From here, you can go to:")
    for room in rooms.get(current_room).get('access'):
        next_room = rooms.get(room).get('label')
        print(f"- {next_room}")

def status_inventory():
    global player_inventory
    global all_items
    if player_inventory.get() == None:
        print("\nYou are not carrying anything")
    else:
        print("\nYou have the following in your inventory:")
        for item in all_items.get('description'):
            print(f"- {item}")

def print_help():
    print("""
    e - (e)xplore room        w - check (w)eapon
    g - (g)o to room
    h - (h)elp (this page)
    i - check (i)nventory
    p - (p)ickup item
    q - (q)uit to terminal
    m - (m)ap""")
