"""
"""

def sumoftens(*numbers):
    sum = 0
    for num in numbers:
        if num <= 9: continue
        num /= 10
        sum += num % 10
    return sum    

print sumoftens(10,123,3453,234,1,6,555)
