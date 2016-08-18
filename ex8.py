# -*- coding: utf-8 -*-
# exercise 8  

formatter = "%r %r %r %r" # it looks like 4 formatters, but in this variable they just strings

# replace the variable formatter with a bunch of numbers  
print formatter % (1,2,3,4) 
# replace the variable formatter with a bunch of strings 
print formatter % ("one", "two", "three", "four") 
# replace the variable formatter with a bunch of Boolean value 
print formatter % (True, False, False, True)
# formatter inside the formatter!!
print formatter % (formatter, formatter, formatter, formatter)
# replace longer strings. 
# when the code is too long, start in a new line with indentation
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)	

