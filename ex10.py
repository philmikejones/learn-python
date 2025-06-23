# Escape sequences

print('I am 5\'11\" tall')

print("\tTabbed in")
print("Split on \nnew line")
print("Include \\ backslashes \\")

print("""A shopping list:
\t* Cat food
\t* Fishsticks
\t* Catnip
""")

# Unicode: https://www.unicode.org/Public/9.0.0/ucd/UnicodeData.txt
print("\N{FIREWORKS}")  # unicode database

apostrophe = "\'"
print('Let{}s try combining escape sequences and string formats'.format(apostrophe))
print(f"Let{apostrophe}s try combining escape sequences and f strings")
