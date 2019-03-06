import matplotlib.pyplot as plt

points = int(input("points: "))
a = float(input("a: "))
x = []
y = []

for i in range(points):
    x_point = -1 + 2*i/points
    x.append(x_point)
    y.append(a*(1-abs(x_point)))

plt.plot(x,y,'k,')
plt.show()