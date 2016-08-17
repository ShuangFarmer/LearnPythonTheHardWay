# -*- coding: utf-8 -*-
# exercise 5  

name = 'Zed A. Shaw'
age = 35 
height = 74 # inches
weight = 180 # lbs
inch = height
pound = weight
centimeter = 2.54 * inch
kilogram = 2.20 * pound

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches or %d centimeters tall." % (height, centimeter)
print "He's %d pounds or %d kilograms heavy." % (weight, kilogram)
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, 100000)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	

	
# notes  

## if changing one variable's name, remember to do so every time this variable appears  

## String Formatting
# Given format % values (where format is a string or Unicode object), 
# % conversion specifications in format are replaced with zero or more elements of values. 

# For more information about String Formatting Operations:
# check Python documentation: https://docs.python.org/2/library/stdtypes.html#string-formatting 5.6.2  

# %r is a very useful one. It's like saying "print this no matter what."
