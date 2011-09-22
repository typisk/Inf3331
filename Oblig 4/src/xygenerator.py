from math import *
import sys, re
usage = 'Usage: %s steps func' % sys.argv[0]
try:
    inp = sys.argv[1] # ex: '0:500,0.5'
    func = sys.argv[2] # ex: 'x*sin(x)'
except:
    print usage; sys.exit(1)
r = eval(inp.split(':')[0]) # also known as start
stop = eval(inp.split(':')[1].split(',')[0]) #get the stop parameter
step = eval(inp.split(',')[1]) # get the step parameter

while r <= stop: 
    x = r 
    print '(%g, %g)' % (x, eval(func)) 
    r += step #increases the step

"""
python xygenerator.py '0:500,0.5' 'x*sin(x)'
(0, 0)
(0.5, 0.239713)
(1, 0.841471)
(1.5, 1.49624)
(2, 1.81859)
(2.5, 1.49618)
(3, 0.42336)
(3.5, -1.22774)
(4, -3.02721)
(4.5, -4.39889)
(5, -4.79462)
....
"""