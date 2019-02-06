import random
from sympy import *

x = symbols('x')
y = random.uniform(0, math.pi)
print(y)
initial = input("function: ")
fxn = sympify(initial)
deriv = diff(fxn, x)
iterations = int(input("How many iterations?"))

for n in range(iterations):
    c = (0.01/(0.01+(fxn.subs(x, y)/deriv.subs(x, y)))) * (fxn.subs(x, y)/deriv.subs(x, y))
    y = y - c

print(y)
