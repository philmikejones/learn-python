import game_functions as g

rooms = {'outside': 'main hall'}

player_room = "Outside"


# Start main game
print("""You are in the forest searching for S.T.A.R.S. Bravo team
when you are ambushed by a pack of dogs.
You run towards a mansion, shooting at the dogs over your shoulder
in a desperate rush for survival.
You burst into the mansion and slam the doors shut.
You are safe, for now...""")

g.status_room(room = player_room)

player_room = g.enter_room('Main hall', current_room = player_room)

g.status_room(room = player_room)

input("> Enter to continue...")

print("""You look around and realise only Barry and Wesker
are in the hall with you.
You go to open the front door to search for your team mates, when
Wesker stops you.
\"Jill, don't open that door!\"
""")
