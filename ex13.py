# Can't use run within VS Code to run this
# Need to call from the command line to add the extra variables

from sys import argv

script, age = argv

print("The script is called: ", script)
print("Your age is: ", age)
print(f"Your age multiplied by 2 is: {int(age) * 2}")
