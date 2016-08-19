# -*- coding: utf-8 -*-
# exercise 14  

from sys import argv

script, user_name = argv

# ***需重复输入的文本放入变量中，后面的代码直接调用此变量。若想改变文本（or 值），仅改变变量这一处***
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)