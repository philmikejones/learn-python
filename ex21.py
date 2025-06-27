def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} and {b}")
    return a * b

x = add(1, 2)
print(x)

y = subtract(3, 2)
print(y)

z = multiply(3, 4)
print(z)

print(z - y * x)

x = int(input("x = ?"))
y = int(input("y = ?"))
print(x + y)
