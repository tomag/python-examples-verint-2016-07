"""
The program receives hosts file as input with format: hostName=ipAddress
and lets the user choose a host and get its ip address.
If the host is not in the list, a message is shown to the user
"""

import sys

entries = {}

if (len(sys.argv) != 2):
    exit("Usage: 01.py <hostsFile>")

(fileName) = sys.argv[1]

with open(fileName, "r") as hosts:
    for line in hosts:
        (hostName, ip) = line.split("=")
        entries[hostName] = ip

print "Write any host name to get its IP address."
print "Press quit to exit."

input = raw_input()
while (input != "quit"):
    if input in entries:
        print "{}={}".format(input, entries[input])
    else:
        print "Entry {} is not in the list".format(input)
    input = raw_input()

print "Good Luck!"        


