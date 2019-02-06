import matplotlib.pyplot as plt

num_try = int(input("how many points to try?"))
trys = int(input("how many iterations per point?"))
accuracy = float(input("accuracy margin: "))
a = float(input("a value: "))
cycle_x = []
y_values = []
basins = []


def cycles(a_1, start_x, iterations):
    y = a_1*start_x*(1-start_x)
    for i in range(iterations):
        if i == (iterations-1):
            cycle_x.append(y)
        y = a_1*y*(1-y)


for b in range(0, num_try):
    point = (4.0/num_try)*b
    cycles(a, point, trys)
    if len(cycle_x) > 1:
        if cycle_x[b] - cycle_x[b-1] > accuracy:
            basins.append(point)

for c in range(len(basins)):
    y_values.append(1)


plt.plot(basins, y_values, 'k.')
plt.show()
