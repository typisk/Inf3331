#!/usr/bin/env python
import sys, math, string

usage = 'Usage: %s outfile t-value infile1 infile2 infileN...' % sys.argv[0]

try:
    outfilename = sys.argv[1]
    t = sys.argv[2]
    infiles = sys.argv[3:]
except:
    print usage; sys.exit(1)

file = 'Some comment here...\n'
file += t + '\n'

data = []

for f in infiles:
    ifile = open(f, 'r')
    file += "\t" + str(f[:-4])
    temp = []
    for line in ifile:
        temp.append(float(line.split()[1]))
    data.append(temp)
    
file += "\n"
for i in range(0, len(data[0])):
    for j in range(0, len(data)):
        file +=  "\t \t " + str(data[j][i])
    file +=  "\n" 

outfile = open(outfilename + '.dat', 'w')
outfile.write(file)
