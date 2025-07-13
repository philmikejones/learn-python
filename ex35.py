import sys

def gold_room():
    print("""You enter a room full of gold. How much do you take?
Enter a number...""")
    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to follow instructions.")

    if how_much < 50:
        print("Nice, you weren't too greedy. You win!")
        sys.exit(0)
    elif how_much >= 50:
        print("You were too greedy.")
        dead("You get eaten by the bear trying to escape with your loot.")

def dead(reason):
    print(reason, "Game over.")
    sys.exit(0)

def bear_room():
    print("You enter a room. In this room is a fierce-looking bear.")
    print("The bear is eating honey")
    print("The bear is blocking the door you want to go through")
    print("How do you move the bear?")
    print("taunt, take honey, or open door")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "taunt":
            print("The bear is sad and moves away from the door")
            print("You can go through the door now")
            bear_moved = True
        elif choice == "take honey":
            print("The bears gets mad")
            dead("The bear slaps you")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not bear_moved:
            print("The bear is still in the way")
            dead("The bear gets mad and takes a swipe at you")
        else:
            dead("I've no idea what that means")

def start():
    print("You approach a crossroads. You can go left or right. Which way do you choose?")
    direction = input("> ")
    if direction == "left":
        bear_room()
    else:
        print("You fall down a hole")
        dead("You fall into the abyss.")

start()
