import sys
from math import sin

print 'Hello World!'

i = 1
while i < len(sys.argv):
    r = float(sys.argv[i])
    print 'sin(%g) = %g' % (r, sin(r))
    i += 1 
    