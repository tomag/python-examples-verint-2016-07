"""
Write a program that takes a file name
and prints line count for the file

Alert the user politely if there was any problem opening the file
"""

import os.path
import sys


fileName = sys.argv[1]

if not (os.path.isfile(fileName)):
    raise IOError("File does not exist") 

with open(fileName) as file:
    for i,l in enumerate(file):
        pass
i+=1
print "Lines: %d" % i
