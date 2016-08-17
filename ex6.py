# -*- coding: utf-8 -*-
# exercise 6

# create a variable and assign strings to it. %d will be replaced by 10
x = "There are %d types of people." % 10 

# create a variable `binary` and assign a string "binary" to it 
binary = "binary"  

# create a variable `do_not` and assign a string "don't" to it
do_not = "don't"  

# create a variable `y` and assign strings to it. 
# %s will be replaced by two variables (binary, do_not) 
# when more than one variable will be replaced, use the format (A, B, C), like a list

y = "Those who know %s and those who %s" % (binary, do_not)

# print the variable x 
print x

# print the variable y
print y

# %r will be replaced by x
print "I said: %r." % x

# %s will be replaced by y
print "I also said: '%s'." % y

# created a variable `hilarious` and assign a boolean value `False` to it.
hilarious = False  

# created a variable `joke_evaluaiton` and assign strings to it
joke_evaluation = "Isn't that joke so funny?! %r"  

# it equivalent to print "Isn't that joke so funny?! %r" % False
print joke_evaluation % hilarious

# create two new variables and assign strings to them
w = "This is the left side of..."
e = "a string with a right side."

# add two variables and print it
print w + e