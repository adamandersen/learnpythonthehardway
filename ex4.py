cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# calculate cars not driven
cars_not_driven = cars - drivers

# amount of drivers gives cars driven
cars_driven = drivers

# the amount of car space for passengers
carpool_capacity = cars_driven * space_in_a_car

# the amount of passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people totay."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
