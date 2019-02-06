from mpmath import *
from sympy import *
cycle = int(input("superstable cycle: "))
start_a = float(input("starting a:"))
iterationsc = int(input("How many newton iterations?"))
temp = start_a
x = symbols('x')
a = symbols('a')

fxn = Mul(Mul(a, x), Add(1, Mul(-1, x)))
for n in range(cycle):
    fxn = Mul(Mul(a, fxn), Add(1, Mul(-1, fxn)))
    simplify(fxn)
    dx = diff(fxn, x)

for m in range(iterationsc):
    d = fxn.subs(x,0.5).subs(a, temp)/dx.subs(x, 0.5).subs(a,temp)
    c = fmul((0.01/(0.01+d)), d)
    temp = fsub(temp, c)

print(temp)
