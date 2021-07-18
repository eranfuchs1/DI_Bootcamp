#For example,  
# my_name = "Frank"  this line creates a name variable type: string 
#print("My name is {}".format(my_name))
cars = 100 # number of cars
print(f'cars is of type: {type(cars)}')
space_in_a_car = 4.0
print(f'space_in_a_car is of type: {type(space_in_a_car)}')
drivers = 30
print(f'drivers is of type: {type(drivers)}')
passengers = 90
print(f'passengers is of type: {type(passengers)}')
cars_not_driven = cars - drivers
print(f'cars_not_driven is of type: {type(cars_not_driven)}')
cars_driven = drivers
print(f'cars_driven is of type: {type(cars_driven)}')
carpool_capacity = cars_driven * space_in_a_car
print(f'carpool_capacity is of type: {type(carpool_capacity)}')
average_passengers_per_car = passengers / cars_driven
print(f'average_passengers_per_car is of type: {type(average_passengers_per_car)}')


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
