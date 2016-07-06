"""
The program receives two numbers as command line arguments
And prints their sum.

If the user did not enter exactly 2 command line arguments,
The usage is printed to the screen. 
"""
import sys

if (len(sys.argv) != 3):
    print "Usage: {} <firstNum> <secondNum>", sys.argv[0]
    sys.exit()

(prName, firstNum, secondNum) = sys.argv

if (firstNum.isdigit() is False or secondNum.isdigit() is False):
    print "Input must be NUMBERS."
    sys.exit()

print int(firstNum) + int(secondNum)