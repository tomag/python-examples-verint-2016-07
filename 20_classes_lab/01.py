"""
The following code assumes a class
named Summer exists. 
Complete the class so correct result is printed
"""

class Summer(object):
    def __init__(self):
        self.sum = 0        

    def add(self, *values):
        for value in values:
            self.sum += value

    def total(self):
        return self.sum


s = Summer()
t = Summer()

s.add(10,20)
t.add(50)
s.add(30)
print s.total()
print t.total()