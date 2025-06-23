cars = 100
spaces_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * spaces_in_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("Therefore, there are", cars_not_driven, "unused cars.")
print("There are", passengers, "passengers wanting a lift.")
print("There are", carpool_capacity, "spaces available if each driver can take 4 passengers.")
print("Each car in the carpool will take, on average,", average_passengers_per_car, "passengers.")
