from sympy import *

x_1, x_2 = symbols('x_1, x_2')
y_1 = float(input("start 1?"))
y_2 = float(input("start 2?"))
initial_1 = (x_1**2) - (3*x_2**2) + 2
initial_2 = x_1 * cos((pi/2)*x_2)
fxn_1 = sympify(initial_1)
fxn_2 = sympify(initial_2)
small = Matrix([[0.01, 0.01], [0.01, 0.01]])
iterations = int(input("How many iterations?"))
for n in range(iterations):
    a = diff(fxn_1, x_1).subs(x_1, y_1).subs(x_2, y_2)
    b = diff(fxn_1, x_2).subs(x_1, y_1).subs(x_2, y_2)
    c = diff(fxn_2, x_1).subs(x_1, y_1).subs(x_2, y_2)
    d = diff(fxn_2, x_2).subs(x_1, y_1).subs(x_2, y_2)
    inv = Matrix([[d, (-1*b)], [(-1*c), a]])
    c = small * (((1/inv.det()) * inv) * Matrix([[fxn_1.subs(x_1, y_1).subs(x_2, y_2)], [fxn_2.subs(x_1, y_1).subs(x_2, y_2)]]))
    y_1 = y_1 - (c.tolist()[0][0]).evalf()
    y_2 = y_2 - (c.tolist()[1][0]).evalf()

print(y_1)
print(y_2)

