"""
The program receives a root directory to search files in, 
and propmts the user with files larger than a minimum size (optional, default 1024KB) and asks the user to delete those files
"""
import os, sys, argparse

def deletionSequence(filePath):
    print "Do you wish to delete the file? [y/n]",
    answer = raw_input()
    if (answer.lower() == "y"):
        os.remove(filePath)

if (len(sys.argv) != 3)
    print "Usage: {} <rootDir> <minSizeInKB>", sys.argv[0]
    sys.exit()
    
(prName, rootDir, minSizeInKB) = sys.argv

for root, dirs, files in os.walk(rootDir):
    for file in files:
        filePath = os.path.join(root, file)
        fileSizeInKB = round(float(os.path.getsize(filePath)) / 1024)
        if (fileSizeInKB > minSizeInKB):
            print "{} {} KB".format(filePath, int(fileSizeInKB))
            deletionSequence(filePath)