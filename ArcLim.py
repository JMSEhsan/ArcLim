from sympy import *
x = symbols('x')
f = 2*(atan (1/(1+x))/sin (atan (1/(1+x)))*(1+x)) - 2*x - pi
result = limit(f, x, oo)
print("Limit of the difference between arc of a half circle with radius of 1 and an arc, which touches the half circle on top, with a chord tending to infinity", result) 