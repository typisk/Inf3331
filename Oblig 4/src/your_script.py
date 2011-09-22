"""
The script will generate values in this format: (x, y)
depending on the input. 

Example of a call:
scriptname.py '0:500,0.5' 'x*sin(x)'

"""
from math import *
import sys
usage = 'Usage: %s steps func' % sys.argv[0]
try:
    inp = sys.argv[1] # ex: '0:500,0.5'
    func = sys.argv[2] # ex: 'x*sin(x)'
except:
    print usage; sys.exit(1)
r = eval(inp.split(':')[0]) # also known as start
stop = eval(inp.split(':')[1].split(',')[0])
step = eval(inp.split(',')[1])
while r <= stop: 
    x = r 
    print '(%g, %g)' % (x, eval(func))
    r += step #increases the step