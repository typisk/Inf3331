from math import sqrt

class Vec3d:
    def __init__(self, i, j, k): 
        self.a = {}
        self.a[0] = i;
        self.a[1] = j;
        self.a[2] = k;        
    
    def __str__(self):
        return '(%g, %g, %g)' % (self.a[0], self.a[1], self.a[2])
    
    def __repr__(self):
        return 'Vec3D(%g, %g, %g)' % (self.a[0], self.a[1], self.a[2])
    
    def __getitem__(self, i): #gets the item
        return self.a[i]
    
    def __setitem__(self, i, v): #set value to class variable
       self.a[i] = v
    
    def __pow__(self, b): #cross product
        return ((self.a[1]*b[2]-self.a[2]*b[1]),
                (self.a[2]*b[0]-self.a[0]*b[2]),
                (self.a[0]*b[1]-self.a[1]*b[0]))
    
    def __add__(self, b): #addition
        return (self.a[0]+b[0], self.a[1]+b[1], self.a[2]+b[2])
    
    def __sub__(self, b): #subtract
        return (self.a[0]-b[0], self.a[1]-b[1], self.a[2]-b[2])
    
    def __mul__(self, b): #multiply
        return self.a[0]*b[0] + self.a[1]*b[1] + self.a[2]*b[2]
    
    def len(self):        #length
        return sqrt(self.a[0]*self.a[0]+self.a[1]*self.a[1]+self.a[2]*self.a[2])u
    
"""
>>> from Vec3D import Vec3d
>>> u = Vec3d(1,0,0)
>>> v = Vec3d(0,1,0)
>>> str(u)
'(1, 0, 0)'
>>> repr(u)
'Vec3D(1, 0, 0)'
>>> u.len()
1.0
>>> u[1]
0
>>> v[2]=2.5
>>> print u**v
(0.0, -2.5, 1)
>>> u+v
(1, 1, 2.5)
>>> u-v
(1, -1, -2.5)
>>> u*v
0.0
"""