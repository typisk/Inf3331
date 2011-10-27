#!/usr/bin/env python
import sys, math, string
from scitools.numpyutils import *

usage = 'Usage: %s infile' % sys.argv[0]

try:
    infilename = sys.argv[1]
except:
    print usage; sys.exit(1)

# load file into a list of lines
f = open(infilename, 'r'); lines = f.readlines(); f.close()

# the second line contains the increment in t:
dt = float(lines[1])

# the third line contains the name of the time series:
ynames = lines[2].split()

# store y data in a dictionary of lists of floats:
y = {}           # declare empty dictionary
for name in ynames:
    y[name] = array([]) # empty list (of y values of a time series)

# load data from the rest of the lines:
for line in lines[3:]:
    yvalues = [float(yi) for yi in line.split()]
    # alternative:  yvalues = map(float, line.split())
    if len(yvalues) == 0: continue  # skip blank lines
    
    i = 0  # counter for yvalues
    for name in ynames:
        
        d = array([yvalues[i]])
        y[name] = append(y[name], d); i += 1

print 'y dictionary:\n', y

# write out 2-column files with t and y[name] for each name:
for name in y.keys():
    ofile = open(name+'.dat', 'w')
    for k in range(len(y[name])):
        ofile.write('%12g %12.5e\n' % (k*dt, y[name][k]))
    ofile.close()
"""
> python convert2_wNumPy.py data.dat
y dictionary:
{'tmp-model2': array([ 1.   ,  0.188,  0.25 ]), 'tmp-model1': array([ 0.1,  0.1,  0.2]), 'tmp-measurements': array([ 0. ,  0.1,  0.2])}

> more tmp-measurements.dat 
           0  0.00000e+00
         1.5  1.00000e-01
           3  2.00000e-01
"""