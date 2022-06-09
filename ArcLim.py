from sympy import *
x = symbols('x')
f = 2*(pi/2-(atan(x)-atan(1/x)))*x/cos((atan(x))-atan(1/x))#2*(atan (1/(1+x))/sin (atan (1/(1+x)))*(1+x)) - 2*x - pi
g = 2*(atan (1/(1+x))/sin(atan (1/(1+x)))*(1+x))
resultf = limit(f, x, oo)
resultg = limit(g, x, 0)
print("Limit of the difference between arc of a half circle with radius of 1 and an arc, which touches the half circle on top, with a chord tending to infinity: ", resultf) 
print("limit 2 : ", resultg)