"""
"""
from random import randint

number = randint(1,100)

print "Pick a number [1-100]"
picked = int(raw_input())
while (picked != number):
    sizeDiff = "smaller" if picked < number else "larger"
    print "The number you picked is {}!".format(sizeDiff)
    print
    print "Pick a number [1-100]"
    picked = int(raw_input())
print "You guess it right!"