# -*- coding: utf-8 -*-
# exercise 12 

age = raw_input("How old are you? ")# 括号内放入想问的问题（字符串），运行时问题会显示在 Terminal
height = raw_input("How tall are you? ") 
weight = raw_input("How much do you weight?" )

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)