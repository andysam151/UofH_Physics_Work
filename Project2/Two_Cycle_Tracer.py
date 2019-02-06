import matplotlib.pyplot as plt

a_value = float(input("what is the a Value? "))
offset = float(input("what is the delta x? "))
traces = int(input("how many trace lines do you want? "))
para_x = [0]
para_y = [0]
cycle_x = []
cycle_y = []


def cycles(a, start_x, iterations):
    x = ((a-1.0)/a)+start_x
    if x > 1:
        print("invalid offset")
    else:
        y = a*x*(1-x)
        cycle_x.append(x)
        cycle_y.append(y)
        for i in range(iterations):
            cycle_x.append(y)
            cycle_y.append(y)
            cycle_x.append(y)
            y = a*y*(1-y)
            if i == iterations-1 and abs(((a-1.0)/a)-cycle_x[i])-0.0001 <= abs(((a-1.0)/a)-cycle_x[0]):
                print("it is a stable 2-cycle")
            elif i == iterations-1:
                print("it escapes a 2-cycle")
            cycle_y.append(y)


for n in range(100000):
    para_x.append((n/100000.0))
    para_y.append((a_value*(n/100000.0)*(1-(n/100000.0))))

cycles(a_value, offset, traces)
plt.plot(cycle_x,cycle_y, 'b', [0, 1], [0, 1], 'k', para_x, para_y, 'k', [cycle_x[len(cycle_x)-1]], [cycle_y[len(cycle_y)-1]], "ro", [cycle_x[0]], [cycle_y[0]], "ko")
plt.show()
