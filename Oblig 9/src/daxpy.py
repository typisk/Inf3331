from numpy import *
import timeit, random


def numpytest(x, y, a): 
    u = a*x+y       #simple
    return u

def pythontest(x,y,a):
    u = []
    for i in x: #for all vector dimensions, doing a*x
        k = [a*m for m in i] #multiplies all elements with a
        u.append(k) 
    for r in range(len(u)):
            for i in range(len(u[r])): #double for loop, doing the addition
                u[r][i] = u[r][i] + y[r][i] # u = (a*x) + y
    return u

a = 5
x1 = array([ [0., 1., 2.], [3., 4., 5.], [6., 7., 8.]])
y1 = array([ [10., 13., 16.], [19., 22., 25.], [28., 31., 34.]])
timer = timeit.Timer(lambda: numpytest(x1, y1, a), "from __main__ import numpytest")
times = timer.timeit(100000)
print "Numpy with array(): %g" % times


x2 = [ [0., 1., 2.], [3., 4., 5.], [6., 7., 8.]]
y2 = [ [10., 13., 16.], [19., 22., 25.], [28., 31., 34.]]
timer2 = timeit.Timer(lambda: pythontest(x2, y2, a), "from __main__ import pythontest")
times2 = timer2.timeit(100000)
print "Normal: %g" % times2

#Numpy without array
timer3 = timeit.Timer(lambda: numpytest(x2, y2, a), "from __main__ import numpytest")
times3 = timer3.timeit(100000)
print "Numpy with x2,y2: %g" % times3

"""
> python daxpy.py
Numpy with array(): 3.74171
Normal: 2.78317
Numpy with x2,y2: 0.291108
"""