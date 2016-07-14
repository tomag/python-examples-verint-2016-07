"""
"""

def mysum(*numbers):
    sum = 0
    for number in numbers:
        if type(number) is int: 
            sum += number
    return sum

def mymul(*numbers):
    mul = 1
    for number in numbers:
        if type(number) is int:
            mul *= number
    return mul

print mysum(1,2,3)
print mysum(1,2,"t",5)
print mymul()
print mymul('foo', 'bla', 10, 20)
