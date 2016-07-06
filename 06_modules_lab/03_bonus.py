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

parser = argparse.ArgumentParser(description= "Runs over files under the given root directory. Prompts deletion message for file larger than minimum size")
parser.add_argument("rootDir", help="Root directory to start checking files")
parser.add_argument("--minSizeInKB", "-mskb", help="Minimum file size to propmt deletion message to user",type=int, default=1024)

args = parser.parse_args()
minSizeInKB = args.minSizeInKB
rootDir = args.rootDir

for root, dirs, files in os.walk(rootDir):
    for file in files:
        filePath = os.path.join(root, file)
        fileSizeInKB = round(float(os.path.getsize(filePath)) / 1024)
        if (fileSizeInKB > minSizeInKB):
            print "{} {} KB".format(filePath, int(fileSizeInKB))
            deletionSequence(filePath)