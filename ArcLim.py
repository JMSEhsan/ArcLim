#Finding limits using sympy
from sympy import *
x = symbols('x')
n = symbols('n')
f = (2*(pi/2-(atan(x)-atan(1/x)))*x/cos(atan(x)-atan(1/x)) - 2*(x-1) - pi).doit()  # just an idea, needs more work
g = x*sin(x)/(1-cos(x))
s = Sum (((sqrt(2) - 1)/sqrt(2))**n,(n,0,oo)).doit()
resultf = limit(f, x, 1.1)
resultg = limit(g, x, 0)
print("the lmit of the difference between arc of a half circle with radius of 1 and an arc, which touches the half circle on top, with a chord tending to infinity:    ", resultf) 
print("Where x --> 0, the limit of g(x) = x*sin(x)/(1-cos(x)) =    ", resultg)
print("Where n from 0 --> + infinity, the divergence limit of the series: Sum (((sqrt(2) - 1)/sqrt(2))^n =    ", s)