# File manipulation
from sys import argv

script, filename = argv

# automatically generate the file so I don't have to keep reproducing it
with open(filename, "w") as file:
    file.write("This is an automatically generated file, created by the ex16.py script\n")

print(f"This script will erase the content of {filename}")
print("The file contains the following data:")
with open(filename, "r") as file:
    print("\t", file.read())
print("-" * 10)
print("If you want to DELETE the contents, press Enter")
print("If you don't want to delete the file, press CTRL-C")
input("What do you want to do?")

file = open(filename, "w")
print(f"Truncating {filename}...")
file.truncate()
print(f"{filename} deleted")
