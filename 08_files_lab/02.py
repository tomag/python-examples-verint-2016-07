"""
"""
import sys
import itertools

if (len(sys.argv) != 4):
    print "Usage: <firstFile> <secondFile> <outputFile>"
    sys.exit()

(first,second,output) = sys.argv[1:]

with open(first, "r") as firstFile:
    with open(second, "r") as secondFile:
        with open(output, "w") as outputFile:
            for line in itertools.izip_longest(firstFile, secondFile, fillvalue=""):
                outputFile.write(line[0])
                outputFile.write(line[1])
