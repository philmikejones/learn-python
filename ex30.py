# Exercise 29 skipped because it was just ifs
people = 30
cars = 40
trucks = 15

def compare_numbers(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return None

biggest_num = compare_numbers(people, cars)
print(f"{biggest_num} is the bigger number")

print("there are more people than cars") if people > cars else print("More cars than people")
