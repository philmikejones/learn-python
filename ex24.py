print('Let\'s practise everything')
print('You\'d need to know about \\ escape sequences too')
print('Including \\n for newlines\n and \\t for \t tab')

poem = """
\t I'm not sure this is a poem as such
But it is a comment using triple-quotes
With a \n newline for good measure
"""

print("-" * 10)
print(poem)
print("-" * 10)

print("Practise f strings")
five = 2 + 3 * 1
print(f"Five is equal to {five}")

def secret_formula(start_value) -> tuple:
    """
    Takes a starting number and calculates the
    number of jars and crates needed for the 
    number of jelly beans

    :returns: jelly_beans, jars, crates
    :rtype: tuple
    """
    jelly_beans = start_value * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return (jelly_beans, jars, crates)

# Tested in pytest
beans, jars, crates = secret_formula(10_000)

print("Apparently there's another way to format a string")
print("Five is still {} but I append with '.format()'".format(five))
print(f"We have {beans} jelly beans, {int(jars)} jars, and that would need {int(crates)} crates")
print("Or I could use .format() again:")
# * in this case is an iterable unpacker
# i.e. secret_formula() returns a tuple which * unpacks to pass to the {}
print("{} beans, {} jars, and {} crates".format(*secret_formula(5000)))
