from sympy import *

a,b,c,e,f,g = symbols('a,b,c,e,f,g')

m1 = Matrix([[a,e,f],[0,b,g],[0,0,c]])
I = Matrix([[1,0,0],[0,1,0],[0,0,2]])
m2 = Matrix([[a,e,f],[0,b,g],[0,0,c]])

pretty_print(m1 ** -1)
pretty_print((m1 ** -1) * I * m1)