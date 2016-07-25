"""
Write a python program that takes numbers in a loop
and for each number prints its square root
If value is negative or not a number show 
a warning and keep reading values
"""
from math import sqrt

def mySqrt(val):
    if not (type(val) == int):
        raise TypeError("Value is not integer")
    elif (val < 0):
        raise ValueError("Value must be greater than 0")
    return sqrt(val)

while True:
    print "Enter a number:",
    val = raw_input()
    try:
        val = int(val)
        print mySqrt(val)
    except ValueError as e:
        print "Failed!!! ", e
    except TypeError as e:
        print "Failed type ", e