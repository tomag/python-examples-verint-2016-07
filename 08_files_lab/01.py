"""
The program receives two files as input
and writes the content of the first file to the second one
"""
import sys

if len(sys.argv) != 3:
    print "Usage: 01.py <firstFile> <secondFile>"
    sys.exit()

(first, second) = sys.argv[1:]

with open(first, "r") as firstFile:
    with open(second, "a") as secondFile:
        for line in firstFile:
            secondFile.write(line)


