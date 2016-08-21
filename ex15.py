# -*- coding: utf-8 -*-
# exercise 15  

# from the library sys import module argv
from sys import argv  

# set two arguments for this script
script, filename = argv  

# open(): Open a file, returning an object of the file type described in section File Objects
# txt is a variable and the value of open(filename) will be assigned to the variable txt
txt = open(filename)

# print the txt
print "Here's your file %r:" % filename
# read() is a function that operate the variable txt 
print txt.read()