import matplotlib.pyplot as plt

points = int(input("points: "))
a = float(input("a: "))
b = float(input("b: "))
x_iter = float(input("initial x: "))
y_iter = float(input("initial y: "))
x = [x_iter]
y = [y_iter]

def inverse_lozi_attractor(a,b,x,y):
    give_x = y/b
    give_y = x - a + pow(y/b, 2)
    return give_x, give_y

for i in range(points):
    x_iter, y_iter = inverse_lozi_attractor(a,b,x_iter,y_iter)
    x.append(x_iter)
    y.append(y_iter)

plt.plot(x,y,'k,')
plt.show()