import sys
from math import sin

print 'Hello World!'
for r in sys.argv[1:]:
    r = float(r)
    print 'sin(%g) = %g' % (r, sin(r))

    