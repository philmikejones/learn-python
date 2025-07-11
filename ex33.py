def add_to_list(start, end):
    
    numbers = []
    
    numbers.extend(range(start, end))

    return numbers

numbers = add_to_list(start = 0, end = 6)
print(numbers)
