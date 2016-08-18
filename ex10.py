# -*- coding: utf-8 -*-
# exercise 10

# escape \  or """

# "I am 6'2\" tall."  # escape double-quote inside string.
# \ 不会出现在 output 里。执行时跳过右邻，右邻功能失效，只是文本
# 'I am 6\'2" tall.'  # escape single-quote inside string


tabby_cat = "\tI'm tabbed in."  
persian_cat = "I'm split\non a line."  
backslash_cat = "I'm \\ a \\ cat."  # I'm \ a \ cat. 
# "\\" 第一个 `\` 让第二个 `\` 失效，第二个 `\` 不再具有 escape 功能，变为普通字符串

# does \t means tab? yes！
fat_cat = """  
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
