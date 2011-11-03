#just getting "None"
import daxpy
from numpy import *

print daxpy.daxpy.__doc__

a = zeros((1,5), order='Fortran')
print isfortran(a)
h = daxpy.daxpy(1, 1.0, a, 1, a, 1)

print h


"""
python daxpy_fortran.py
daxpy - Function signature:
  daxpy(n,da,dx,incx,dy,incy)
Required arguments:
  n : input int
  da : input float
  dx : input rank-1 array('d') with bounds (*)
  incx : input int
  dy : input rank-1 array('d') with bounds (*)
  incy : input int

True
None
"""