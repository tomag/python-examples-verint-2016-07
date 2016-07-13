"""
"""

startIndex = 97
totalLetters = 26

letters = [chr(i) for i in range(startIndex, startIndex + totalLetters)]

allOptions = ["{}{}{}".format(i,j,k) for i in letters for j in letters for k in letters]

print allOptions