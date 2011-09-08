import sys
from math import log

print 'Hello World!'

i = 1
while i < len(sys.argv):
    r = float(sys.argv[i])
    if (r > 0):
        print 'log(%g) = %g' % (r, log(r))
    else:
        print 'log(%g) is illegal' % r
    i += 1