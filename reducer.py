__author__ = 'topsolver'

import sys

key = None
val = 0
for line in sys.stdin:
    curkey,curval = line.strip().split(",")
#    print parts
    if (curkey != key):
        if (key != None):
            print key.strip()+","+str(val)
        val = float(curval)
        key = curkey

    else:
        val += float(curval)

    #print parts[2].strip()+","+parts[2].strip()

if (key != None):
    print key.strip()+","+str(val)

