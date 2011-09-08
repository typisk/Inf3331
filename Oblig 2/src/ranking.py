import os, sys, re

usage = 'Usage: %s testfile' % sys.argv[0]

try:
    infile = sys.argv[1]
except:
    print usage; sys.exit(1)
    
data = {}
testfile = open(infile, 'r')
for line in testfile:
    match = re.search(r"CPU-time:\s+((\d+\.\d*|\d*\.\d+)|(\d+))\s+(.*)", line)
    if match:
        data[match.group(1)] = match.group(4)


dats =  sorted((float(x),y) for x,y in data.iteritems())

for key,value in dats:
    print "%.2f:\t %s" % (float(key), value) 