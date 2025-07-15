default_prompt = "> Press Enter to continue..."

rooms = {
    "outside" : {
      "label" : "Outside",
      "key"   : None,
      "access" : ("mainhall")
    },
    "mainhall" : {
      "label"  : "Main hall",
      "key"    : None,
      "access" : ("diningroom", "artroom")
    },
    "diningroom" : {
      "label" : "Dining room",
      "key"   : None,
      "access" : ("mainhall", "westgroundcorridor")
    },
    "westgroundcorridor" : {
      "label"  : "West Ground Corridor",
      "key"    : None,
      "access" : ("diningroom", "musicroom")
    },
    "musicroom" : {
      "label" : "Music room",
      "key"   : "armour",
      "access" : "westgroundcorridor"
    },
    "artroom" : {
      "label" : "Art room",
      "key"   : "Armour",
      "access" : ("mainhall")
    }
}

player_room = 'outside'


def enter_room(current_room, new_room):
    global rooms
    # strip whitespace and make lowercase to make string comparison easier
    current_room_flat = current_room.lower().replace(" ", "")
    new_room_flat = new_room.lower().replace(" ", "")
    # Check the proposed room can be entered from where the player's current room
    if new_room_flat not in rooms[current_room_flat]["access"]:
        print(f"You cannot enter the {new_room} from {current_room}.")
        return current_room
    return new_room

def status_room(current_room):
    global rooms
    # standardise string for easier lookup
    current_room = current_room.lower().replace(" ", "")
    print_room = rooms[current_room]['label']
    print(f"You are currently in the {print_room}")
    print("From here, you can go to:")
    for room in rooms[current_room]['access']:
        next_room = rooms[room]['label']
        print(f"- {next_room}")

def print_help():
    print("g - (g)o to room")
    print("h - (h)elp (this page)")
    print("q - (q)uit to terminal")
    print("m - (m)ap")


## Start main game
# status_room(player_room)
print("""\nYou are in the forest searching for S.T.A.R.S. Bravo team
when you are ambushed by a pack of dogs.
You run towards a mansion, shooting at the dogs over your shoulder
in a desperate rush for survival.
You burst into the mansion and slam the doors shut.
You are safe, for now...\n""")

player_room = enter_room(player_room, 'Main hall')
input(default_prompt)

# status_room(player_room)
print("""\nYou look around and realise only Barry and Wesker
are in the hall with you.
You go to open the front door to search for your team mates, when
Wesker stops you.
\"Jill, don't open that door!\"\n""")

input("> Press any key to continue...")

print("""\nYou hear a gunshot in a distant part of the mansion.
Wesker orders you and Barry to investigate.
You follow Barry through one of the side doors
and find yourself in a grand dining room.\n""")

player_room = enter_room(player_room, 'dining room')
# status_room(player_room)

default_prompt = "> What do you do next? (h for help)"

while True:
    action = input(default_prompt)
    if action == 'h':
        print_help()
    elif action == 'g':
        status_room(player_room)
        prompt_room = input("> Which room will you go to?")
        player_room = enter_room(player_room, prompt_room)
        status_room(player_room)
    elif action == 'm':
        status_room(player_room)
    elif action == 'q':
        exit(0)
    else:
        print("I didn't understand that. Try again")
