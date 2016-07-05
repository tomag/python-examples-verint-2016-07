"""
    Input: None
    Process: Randomize numbers [1,100000] until finding a number divides by 7,13,15
"""
from random import randint

def checkDiv(num):
    return num % 7 == 0 and num % 13 == 0 and num % 15 == 0

num = randint(1,100000)
while (checkDiv(num)):
    num = randint(1,100000)    

print num