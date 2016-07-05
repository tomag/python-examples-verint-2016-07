"""
    Input: None
    Process: Randomize 7 numbers
    Output: 
        1. Prints sum of all numbers.
        2. If sum % 7 == 0 then print 'Boom'
"""
from random import randint

totalNumber = 7
sum = 0
while (totalNumber > 0):
    sum += randint(1,100)
    totalNumber-=1
print "Sum: ", sum,
if sum % 7 == 0: print "Boom!"