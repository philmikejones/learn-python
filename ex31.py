print("""You go through a room with two doors.
Do you enter door 1 or door 2?""")

door = int(input("Door 1 or 2? > "))

if door == 1:
    print("""You chose door number 1.
    Behind the door is a bear who eats you. The end.    
    """)
elif door == 2:
    print("""You chose door number 2.
    Behind the door are unimaginable riches. Well done.
    """)
    spend = input("Do you spend or save your new riches?")
    if spend == 'spend':
        print("You spend your money and die happy having enjoyed your riches")
    elif spend == 'save':
        print("You save your money and die joyless")
    else:
        print("You did not follow instructions. The bear eats you.")
else:
    print("You did not enter 1 or 2. Clearly you can't follow instructions. The bear eats you.")

print("Choose a number between 1 and 10")
number = int(input("> "))

if number in range(5):
    print("Less than 5")
elif number < 0:
    print("You provided a negative number")
else:
    print("5 or greater")
