# -*- coding: utf-8 -*-
# exercise 13  

from sys import argv # sys: library argv: module

script, space, time = argv

print "The script is called: ", script
print "which planet you are living? ", space
print "what time is it now? ", time

animation = raw_input("The animation you recently watched:")
song = raw_input("The song you recently listen to:" )

# when runing the code in Terminal, 
# remember to input arguments  
# $ python ex13.py first 2nd 3rd