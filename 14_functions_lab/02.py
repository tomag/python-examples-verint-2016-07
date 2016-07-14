"""
"""

import sys

def isrighttype(number, text):
    if number.isdigit() == False:
        raise Exception("Input '{}' is not a valid number".format(number))

if len(sys.argv) != 3:
    sys.exit("Usage: 02.py <number> <string>")

(number, text) = sys.argv[1:]

isrighttype(number, text)
