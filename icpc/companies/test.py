from sympy import *

a = symbols('a')

m1 = Matrix([[1,0,a],[0,1,0],[0,0,1]])
m2 = Matrix([[1,0,-a],[0,1,0],[0,0,1]])

print(m1**-1)

pretty_print(m1**-1)
