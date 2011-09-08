#!/usr/bin/env python
                                        # fault - whitespace between /bin and /env
import sys, random
def compute(n):
    i = 0; s = 0
    while i <= n:
        s += random.random()
        i += 1                          # fault - invalid indent
    return s/n

n = int(sys.argv[1])                    # fault - needs to be int
print 'the average of %d random numbers is %g' % (n, compute(n)) 
                                        #fault - " instead of '