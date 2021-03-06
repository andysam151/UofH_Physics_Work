import matplotlib.pyplot as plt

a_value = float(input("what is the a Value? "))
cycle = int(input("cycle: "))
cycle_x = []
cycle_y = []


def cycles(a, start_x, iterations):
    y = start_x
    for i in range(iterations):
        y = a*y*(1-y)
    cycle_x.append(4*start_x)
    cycle_y.append(y)


for n in range(0, 1000):
    cycles(a_value, n/1000.0, cycle)

plt.plot(cycle_x, cycle_y, 'b', [0, 4], [0, 1], 'k')
plt.show()
