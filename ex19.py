def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses")
    
    if boxes_of_crackers == 0:
        print("We've forgotten the crackers, Gromit!")
    else:
        print(f"You have {boxes_of_crackers} boxes of crackers.")

# Pass the numbers to the function directly
cheese_and_crackers(10, 0)

# Or use variables
num_cheese = 10
num_crackers = 7
cheese_and_crackers(num_cheese, num_crackers)

# Can do maths with arguments
cheese_and_crackers(10 + num_cheese, num_crackers - 7)

# Ask for user input
num_cheese = int(input("How much cheese?: "))
num_crackers = int(input("How many boxes of crackers?: "))
cheese_and_crackers(num_cheese, num_crackers)
