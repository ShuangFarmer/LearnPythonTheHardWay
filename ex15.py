# -*- coding: utf-8 -*-
# exercise 15  

# from the library sys import module argv
#from sys import argv  

# set two arguments for this script
#script, filename = argv  

# open(): Open a file, returning an object of the file type described in section File Objects
# ok, file object is the DVD player not the DVD itself
# txt is a variable and the value of open(filename) will be assigned to the variable txt
filename = raw_input("what is your file name?" )
txt = open(filename)

# print the txt
print "Here's your file %r:" % filename
# read() is a function/method that operate the variable txt, AKA an object 
print txt.read()
txt.close()

## notes  
# run open() in the shell  
# $ open("filename") <- get an object  
# output: <open file 'ex15_sample.txt', mode 'r' at 0x10ee175d0>  
# $ open("filename").read <- read the text

#  It's important to close files when you are done with them by using the method: .close()