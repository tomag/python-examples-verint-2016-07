"""
The program receives a number as command line arguemnt
And prints "Hello Python" multiple time (according to the given number)
"""
import sys

repeatCount = int(sys.argv[1])
while repeatCount > 0:
    print "Hello Python"
    repeatCount-=1