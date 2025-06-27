from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_line(line_count, f):
    print(line_count, f.readline(), end = "")

current_file = open(input_file)

print("First print the whole file")
print_all(current_file)

print("Now rewind, like a tape")
rewind(current_file)

print("Now print first line")
current_line = 1
print_line(current_line, current_file)
current_line += 1
print_line(current_line, current_file)
current_line += 1
print_line(current_line, current_file)
current_line += 1
print_line(current_line, current_file)
# current_line + 1... increments the count; this DOES NOT tell the function which line to read
# It just increments as you readline()
