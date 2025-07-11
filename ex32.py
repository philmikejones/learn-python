the_count = []
for i in range(1, 6):
    the_count.append(i)

fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f'This is count {number}')

for fruit in fruits:
    print(fruit)

for i in change:
    print(f'You got: {i}')

elements = []
# print(elements)
# for i in range(0, 6):
#     print(f'Adding {i} to elements')
#     elements.append(i)

# Instead of for loop with append you can use .extend()
# https://stackoverflow.com/a/42437638
elements = elements.extend(range(6))

print(elements)
