cars = 100
spaces_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * spaces_in_car
average_passengers_per_car = passengers / cars_driven

print(f'There are {cars} in the carpool')
print(f'There are {drivers} drivers')
print(f'There are {cars_not_driven} empty cars')
print(f'There are {int(carpool_capacity)} spaces available (if each car takes {int(spaces_in_car)} passengers)')
print(f'There are {passengers} passengers')
print(f'Each car should take {int(average_passengers_per_car)} passengers')
