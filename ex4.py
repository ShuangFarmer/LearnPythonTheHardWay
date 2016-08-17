# -*- coding: utf-8 -*-
# exercise 4  

cars = 100  
space_in_a_car = 4.0  # 4.0 为浮点数，浮点数的运算结果也为浮点数
drivers = 30  
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven  

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."  
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."  
print "We have", passengers, "to carpool today."  
print "We need to put about", average_passengers_per_car, "in each car."

# notes  

# add space around operators so that it's easier to read.  










