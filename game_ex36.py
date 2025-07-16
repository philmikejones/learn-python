import os
# clear the terminal
# https://stackoverflow.com/a/2084628
os.system('cls' if os.name == 'nt' else 'clear')

default_prompt = "> Press Enter to continue..."

rooms = {
    "outside" : {
      "label"  : "Outside",
      "key"    : None,
      "access" : ("mainhall",),  # need to force a tuple or python will iterate over the invididual letters
      "items"  : None,
    },
    "mainhall" : {
      "label"  : "Main hall",
      "key"    : None,
      "access" : ("diningroom", "artroom"),
      "items"  : None,
      "description" : "The Main hall of this mysterious mansion. A grand staircase sweeps up to the first floor. It is too dangerous to go back outside."
    },
    "diningroom" : {
      "label"  : "Dining room",
      "key"    : None,
      "access" : ("mainhall", "westgroundcorridor"),
      "items"  : ("Emblem", ),
      "trigger_special" : False,
      "description" : "An elaborate dining room with a ticking clock and a fireplace at the far end of the room. There is blood in front of the fireplace."
    },
    "westgroundcorridor" : {
      "label"  : "West Ground Corridor",
      "key"    : None,
      "access" : ("diningroom", "musicroom"),
      "items"  : ("Clip",),
      "description" : "A long corridor connecting the rooms of the west side of the house. The corpse of Kenneth from Bravo team is at the end of the hallway."
    },
    "musicroom" : {
      "label"  : "Music room",
      "key"    : "armour",
      "access" : ("westgroundcorridor",),
      "items"  : ("Gold emblem", "Music sheet"),
      "description" : "A music room with grand piano, a drinks bar, a bookcase, and what looks like a gap in the wall..."
    },
    "artroom" : {
      "label"  : "Art room",
      "key"    : "Armour",
      "access" : ("mainhall", "eastgroundcorridor"),
      "items"  : None,
      "description" : "A room with a marble statue, various paintings, and art supplies tucked around the corner on shelves."
    },
    "eastgroundcorridor" : {
      "label" : "East Ground Corridor",
      "key"   : None,
      "access" : ("artroom", "eastgroundrearcorridor"),
      "items" : ("clip", ),
      "description" : "A long corridor with ornate silverware and crockery stored in sideboards. The corridor takes you to the back of the mansion."
    },
    "eastgroundrearcorridor" : {
      "label" : "East Ground Rear Corridor",
      "key"   : None,
      "access" : ("eastgroundcorridor",),
      "items": None,
      "description" : "A winding corridor that takes you to the rear of the mansion. There is a bathroom, a study, and an outside store accessed from this corridor. Otherwise it is pretty unremarkable."
    },
}

player_room = 'outside'
player_health = int(100)
player_inventory = ['knife', 'pistol']
equipped_weapon = None

all_items = {
    'knife' : {
        'description' : 'A combat knife.',
        'type' : 'melee'
    },
    'pistol' : {
        'description' : 'Your pistol. Takes 15mm rounds',
        'type' : 'weapon'
    }
}

player_pistol_ammo = int(15)
player_shotgun_ammo = int(0)
player_magnum_ammo = int(0)

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
    if player_inventory.get() == None:
        print("\nYou are not carrying anything")
    else:
        print("\nYou have the following in your inventory:")
        for item in player_inventory.get('description'):
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


## Start main game
# status_room(player_room)
print("""\nYou are in the forest searching for S.T.A.R.S. Bravo team
when you are ambushed by a pack of dogs.
You run towards a mansion, shooting at the dogs over your shoulder
in a desperate rush for survival.
You burst into the mansion and slam the doors shut.
You are safe, for now...""")

player_room = enter_room(player_room, 'Main hall')
input(default_prompt)

# status_room(player_room)
print("""\nYou look around and realise only Barry and Wesker
are in the hall with you.
You go to open the front door to search for your team mates, when
Wesker stops you.
\"Jill, don't open that door!\"""")

input(default_prompt)

print("""\nYou hear a gunshot in a distant part of the mansion.
Wesker orders you and Barry to investigate.
You follow Barry through one of the side doors
and find yourself in a grand dining room.""")

input(default_prompt)
player_room = enter_room(player_room, 'dining room')
# status_room(player_room)

print("""\nBarry moves slowly with his weapon drawn. You follow, wondering what kind of nightmare you've found yourself in.
Barry notices a pool of blood by the fireplace and bends down to investigate. The blood hasn't dried yet, so is recent.
You hope it isn't Chris's blood. Barry says he will investigate here a bit more and you continue your search. """)

input(default_prompt)
player_room = enter_room(player_room, 'west ground corridor')

print("""\nYou are in a long, dimly lit corridor. You hear a crunching so you investigate.
Round a corner you see a figure hunched over a body. It's clearly wearing a S.T.A.R.S. uniform
and you realise to your horror that the figure is feasting on your team mate, Kenneth, from Bravo team.
The figure notices you, slowly gets up and starts to shuffle towards you, arms outstretched.
You are so shocked by what you've seen you forget your training and instead turn to flee.""") 

input(default_prompt)
player_room = enter_room(player_room, 'dining room')

print("""\nYou burst back in to the dining room with the creature that was eating Kenneth following you.
You shout at Barry for help. Barry shoots at the creature but it doesn't stop.
Barry shoots it again, until it finally collapses. You are shaken, but alive.
You catch your breath, and decide to report this to Wesker.
""")

input(default_prompt)
player_room = enter_room(player_room, 'main hall')
print("""\nYou return to the main hall, but Wesker isn't there.
You and Barry briefly search the Main hall but he's nowhere to be found.
Barry suggests you split up to look for him before handing you a LOCKPICK.
He say's he'll go back to the dining room, and you will start looking
on the east side of the house (ART ROOM).
Barry turns and leaves.""")

default_prompt = "\n> What do you do next? (h for help) "

while True:
    action = input(default_prompt)
    if action == 'h':
        print_help()
    elif action == 'e':
        explore_room(player_room)
    elif action == 'g':
        status_room(player_room)
        prompt_room = input("\n> Which room will you go to? ")
        player_room = enter_room(player_room, prompt_room)
        status_room(player_room)
    elif action == 'm':
        status_room(player_room)
    elif action == 'p':
        prompt_item = input("> Which item will you pick up? ")
        print(prompt_item)
    elif action == 'w':
        if equipped_weapon == None:
            print("\nYou do not have a weapon equipped.")
        else:
            print(f"\nYour {equipped_weapon} is equipped.")
        print("You can equip the following weapon(s):")
        for item in player_inventory:
            print(f"- {item}")
        prompt_weapon = input("> Equip/change weapon? (y/n) ")
        if prompt_weapon == "y":
            which_weapon = input("> Which weapon? ")
        elif prompt_weapon == "n":
            continue
        else:
            print("Sorry, I didn't understand that. Try again.")
    elif action == 'q':
        exit(0)
    else:
        print("I didn't understand that. Try again")
