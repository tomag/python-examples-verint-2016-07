"""
    Input: 10 numbers
    Output: Maximum number
"""
totalNumbers = 10

def getUserInput(inputIndex):
    print "Number {}: ".format(inputIndex),
    input = int(raw_input())    
    return input

inputIndex = 1
max = getUserInput(inputIndex)

for num in range(1,totalNumbers,1):
    inputIndex+=1
    input = getUserInput(inputIndex)    
    if (input > max):
        max = input
print "Max = ", max


