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
        if (type(b) == type(self)):
            return (self.a[0]+b[0], self.a[1]+b[1], self.a[2]+b[2]) #vector + vector
        else:
            return (self.a[0]+b, self.a[1]+b, self.a[2]+b) #scalar + vector
    
    def __sub__(self, b): #subtract
        if (type(b) == type(self)):
            return (self.a[0]-b[0], self.a[1]-b[1], self.a[2]-b[2]) #vector - vector
        else:
            return (self.a[0]-b, self.a[1]-b, self.a[2]-b) #scalar - vector
    
    def __mul__(self, b): #multiply
        if (type(b) == type(self)):
            return self.a[0]*b[0] + self.a[1]*b[1] + self.a[2]*b[2] #vector * vector
        else:
            return self.a[0]*b + self.a[1]*b + self.a[2]*b #vector * scalar
    
    def __rmul__(self, b): #multiply
        if (type(b) == type(self)):
            return self.a[0]*b[0] + self.a[1]*b[1] + self.a[2]*b[2] #vector * vector
        else:
            return self.a[0]*b + self.a[1]*b + self.a[2]*b #vector * scalar
            
    def __radd__(self, b): # b + self
        if (type(b) == type(self)):
            return (b[0]+self.a[0], b[1]+self.a[1], b[2]+self.a[2]) #vector + vector
        else:
            return (b+self.a[0], b+self.a[1], b+self.a[2]) #scalar + vector
    
    def __rsub__(self, b): # b - self
        if (type(b) == type(self)):
            return (b[0]-self.a[0], b[1]-self.a[1], b[2]-self.a[2]) #vector - vector
        else:
            return (b-self.a[0], b-self.a[1], b-self.a[2]) #scalar - vector
    def __div__(self, b):
        return (self.a[0]/b, self.a[1]/b, self.a[2]/b) #scalar / vector
        
    def len(self):        #length
        return sqrt(self.a[0]*self.a[0]+self.a[1]*self.a[1]+self.a[2]*self.a[2])
    
"""
>>> from Vec3D_ext import Vec3d
>>> u = Vec3d(1, 0, 0)
>>> v = Vec3d(0, -0.2, 8)
>>> a = 1.2
>>> u+v
(1, -0.2, 8)
>>> 
>>> a+v
(1.2, 1.0, 9.2)
>>> v+a
(1.2, 1.0, 9.2)
>>> a-v
(1.2, 1.4, -6.8)
>>> v-a
(-1.2, -1.4, 6.8)
>>> a*v
9.36
>>> v*a
9.36
>>> v/a
(0.0, -0.16666666666666669, 6.666666666666667)
"""