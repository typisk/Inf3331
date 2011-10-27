from scitools.numpyutils import *

a = array([[1, 2, 3], [4, 5, 7], [6, 8, 10]], float)
b = array([-3, -2, -1], float)

print multiply(a,b)

"""
python matvec.py

[[ -3.  -4.  -3.]
 [-12. -10.  -7.]
 [-18. -16. -10.]]
"""

