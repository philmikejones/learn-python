import os
import game_functions as funcs
import game_rooms as rooms

## clear the terminal
## https://stackoverflow.com/a/2084628
os.system('cls' if os.name == 'nt' else 'clear')


## Start main game
player_room = 'outside'
default_prompt = "> Press Enter to continue..."

# status_room(player_room)
print("""\nYou are in the forest searching for S.T.A.R.S. Bravo team
when you are ambushed by a pack of dogs.
You run towards a mansion, shooting at the dogs over your shoulder
in a desperate rush for survival.
You burst into the mansion and slam the doors shut.
You are safe, for now...""")

player_room = funcs.enter_room(player_room, 'Main hall')
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
player_room = funcs.enter_room(player_room, 'dining room')
# status_room(player_room)

print("""\nBarry moves slowly with his weapon drawn. You follow, wondering what kind of nightmare you've found yourself in.
Barry notices a pool of blood by the fireplace and bends down to investigate. The blood hasn't dried yet, so is recent.
You hope it isn't Chris's blood. Barry says he will investigate here a bit more and you continue your search. """)

input(default_prompt)
player_room = funcs.enter_room(player_room, 'west ground corridor')

print("""\nYou are in a long, dimly lit corridor. You hear a crunching so you investigate.
Round a corner you see a figure hunched over a body. It's clearly wearing a S.T.A.R.S. uniform
and you realise to your horror that the figure is feasting on your team mate, Kenneth, from Bravo team.
The figure notices you, slowly gets up and starts to shuffle towards you, arms outstretched.
You are so shocked by what you've seen you forget your training and instead turn to flee.""") 

input(default_prompt)
player_room = funcs.enter_room(player_room, 'dining room')

print("""\nYou burst back in to the dining room with the creature that was eating Kenneth following you.
You shout at Barry for help. Barry shoots at the creature but it doesn't stop.
Barry shoots it again, until it finally collapses. You are shaken, but alive.
You catch your breath, and decide to report this to Wesker.
""")

input(default_prompt)
player_room = funcs.enter_room(player_room, 'main hall')
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
        funcs.print_help()
    elif action == 'e':
        funcs.explore_room(player_room)
    elif action == 'g':
        funcs.status_room(player_room)
        prompt_room = input("\n> Which room will you go to? ")
        player_room = funcs.enter_room(player_room, prompt_room)
        status_room(player_room)
    elif action == 'i':
        funcs.status_inventory()
    elif action == 'm':
        funcs.status_room(player_room)
    elif action == 'p':
        prompt_item = input("> Which item will you pick up? ")
        print(prompt_item)
    elif action == 'q':
        exit(0)
    else:
        print("I didn't understand that. Try again")
