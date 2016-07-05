"""
"""
from random import randint

checkers = [2,3,5,7]
def getPrimes(num):
    primes = {} 
    for checker in checkers:
        primes[checker] = 0        
        while (num % checker == 0):
            primes[checker]+=1
            num /= checker
    return primes

firstNum = randint(1,10)
firstPrimes = getPrimes(firstNum)
secondNum = randint(1,10)
secondPrimes = getPrimes(secondNum)
 
print "First: {}. Primes: {}".format(firstNum, firstPrimes)
print "Second: {}. Primes: {}".format(secondNum, secondPrimes)

multiple = 1
for checker in checkers:
    maxTimes = max(firstPrimes[checker], secondPrimes[checker])
    if (maxTimes != 0):
        multiple *= maxTimes * checker
print "Multiple: ", multiple