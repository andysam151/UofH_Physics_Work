from sympy import *
itterations = int(input("cycle: "))
a = float(input("a: "))
x = symbols('x')
fxn = Mul(Mul(a,x),Add(1,Mul(-1,x)))

for n in range(itterations):
    fxn = Mul(Mul(a,fxn),Add(1,Mul(-1,fxn)))
simplify(fxn)
dx = diff(fxn, x)

