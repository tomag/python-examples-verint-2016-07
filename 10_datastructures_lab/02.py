"""
The program receives input file containing a word in each line.
Prints all anagrams in the same line
"""

import sys
from collections import Counter

if (len(sys.argv) != 2):
    exit("Usage: 02.py <fileName>")

fileName = sys.argv[1]

repeats = {}

with open(fileName, "r") as fin:
    for line in fin:
        line = line.rstrip()
        sortedLine = ''.join(sorted(line))
        if sortedLine in repeats:
            repeats[sortedLine].append(line)
        else:
            repeats[sortedLine] = [line]

for values in repeats.values():
    for value in values:
        print value,
    print