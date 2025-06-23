# Can't use VS Code Run
# Call from terminal and add filename (ex15-content.txt) as a command line argument

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Your file is called {filename}.")
print(f"Below are its contents:")
print(txt.read())
txt.close()

print("Try by prompting the user for the filename")
filename = input("What is the name of the file to read? ")

txt = open(filename)
print(txt.read())
txt.close()
