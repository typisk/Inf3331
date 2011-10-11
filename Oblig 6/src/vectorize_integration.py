from scitools.all import *

n = 1000
a = 0.0           # x = 0
b = 4.0           # x = 4
sum = 0.0


for x in linspace(a, b, n):
    g = lambda x: 1+x   
    h = (b-a)/(n-1.0)
    sum += (h/2)*( g(a) + g(b))
    
    # h*sum(i=1,...n-1) f(a+i*h) ???