"""
    Input: None
    Process: Randomize number between 1 to 10,000
    Output: Sum of digits of the random number
"""
from random import randint

number = randint(1,10000)
print "Number: ", number
sum = 0

print "Digits: ",
while number > 0:
    digit = number % 10
    print digit,
    sum += digit     
    number /= 10
print
print "Sum of Digits: ", sum