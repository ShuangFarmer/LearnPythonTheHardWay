# -*- coding: utf-8 -*-
# exercise 11  

print "How old are you?", # 逗号表示 print 第一句和逗号承接的下一句
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)