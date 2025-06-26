def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}; arg2: {arg2}")

# Don't need the *args
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}; arg2: {arg2}")

print_two("Phil", "First")
print_two_again("Phil", "Again")
