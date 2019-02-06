import matplotlib.pyplot as plt
import random

start_a = float(input("Starting a: "))
increment = float(input("increment: "))
num_try = int(input("number of points to try: "))
trys = int(input("iterations per point: "))
accuracy = float(input("accuracy margin: "))
cycle_x = []
final_y = []
a_values = []


def cycles(a, start_x, iterations):
    y = a*start_x*(1-start_x)
    for i in range(iterations):
        if i == (iterations-1):
            cycle_x.append(y)
        y = a*y*(1-y)


for n in range(int(start_a/increment), int(4/increment)):
    m = increment * n
    attractors = []
    cycle_x = []
    for b in range(0, num_try):
        point = random.uniform(0, 1)
        cycles(m, point, trys)
        if len(attractors) > 0:
            for g in range(len(attractors)):
                if abs(attractors[g]-cycle_x[b]) <= accuracy:
                    break
                elif g == (len(attractors)-1) and abs(attractors[g]-cycle_x[b]) >= accuracy:
                    attractors.append(cycle_x[b])
                    break
        elif b == 0:
            attractors.append(cycle_x[0])
    for c in range(len(attractors)):
        final_y.append(attractors[c])
        a_values.append(m)


plt.plot(a_values, final_y, 'k,')
plt.show()
