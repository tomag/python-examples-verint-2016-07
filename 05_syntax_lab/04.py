"""
    Input: Lines from user, until empty line
    Output: All lines from user, from the end to beginning
"""
import sys

inputList = []
inputIndex = 1

def getInputFromUser(inputIndex):
    print "Line {}: ".format(inputIndex),
    input = raw_input()
    return input

print
print "Enter lines as you wish. Press Another ENTER to finish"
input = getInputFromUser(inputIndex)

while (len(input) > 0):
    inputIndex+=1
    inputList.insert(0, input)
    input = getInputFromUser(inputIndex)    

if (len(inputList) == 0):
    print "you did not enter any input. Exiting...".capitalize()
    sys.exit()
    
print
print "you entered:".title()

index = 1
for line in inputList:
    print "{}. ".format(index), line
    index+=1