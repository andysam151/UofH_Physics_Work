import matplotlib.pyplot as plt

cycle_x = []
para_x = [0]
para_y = [0]
last_x = []
last_y = []
cycle = int(input("superstable cycle: "))
a = float(input("a:"))

cycle_x.append([0.5, a/4])
for m in range(cycle):
    cycle_x.append([cycle_x[m][1], a*cycle_x[m][1]*(1-cycle_x[m][1])])

for n in range(100000):
    para_x.append((n/100000.0))
    para_y.append((a*(n/100000.0)*(1-(n/100000.0))))

for l in range(len(cycle_x)):
    last_x.append(cycle_x[l][0])
    last_y.append(cycle_x[l][1])

plt.plot(last_x, last_y, 'b', [0, 1], [0, 1], 'k', para_x, para_y, 'k')
plt.show()
