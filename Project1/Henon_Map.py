import matplotlib.pyplot as plt

points = int(input("points: "))
a = float(input("a: "))
b = float(input("b: "))
x_iter = float(input("initial x: "))
y_iter = float(input("initial y: "))
x = [x_iter]
y = [y_iter]

def henon_attractor(a,b,x,y):
    give_x = y + a - pow(x, 2)
    give_y = x * b
    return give_x, give_y

for i in range(points):
    x_iter, y_iter = henon_attractor(a,b,x_iter,y_iter)
    x.append(x_iter)
    y.append(y_iter)

plt.plot(x,y,'k,')
plt.show()