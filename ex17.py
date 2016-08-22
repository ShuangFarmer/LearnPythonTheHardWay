# -*- coding: utf-8 -*-
# exercise 17 

from sys import argv

# if exists returns True, it means a file exists.
# from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())
