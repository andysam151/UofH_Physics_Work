import math
import matplotlib.pyplot as plt

cycle = int(input("superstable cycle: "))
start_a = float(input("starting a:"))
trys = int(input("How many newton trys?"))


def cycles(a, start_x, iterations):
    y = a*start_x*(1-start_x)
    for i in range(iterations):
        store.append(y)
        y = a*y*(1-y)


for n in range(trys):
    store = []
    deriv = []
    double_deriv = []
    cycles(start_a,0.5,cycle)
    for m in range(cycle):
        if m == 0:
            deriv.append(start_a*(1-(2*store[m])))
            double_deriv.append(start_a * (1 - (2 * deriv[m])))
        else:
            deriv.append((start_a * (1 - (2 * store[m])))*deriv[m-1])
            double_deriv.append((start_a * (1 - (2 * deriv[m]))) * double_deriv[m - 1])
    if double_deriv[len(double_deriv)-1] == 0:
        print(double_deriv[len(double_deriv) - 1])
        print("Stopped")
        break
    d = deriv
    c = (deriv.pop())/double_deriv.pop()
    correction = 0.01/(0.01 + abs(c))
    start_a = start_a - (correction*c)

print(start_a)
print(len(d))
plt.plot(store, d, 'k,')
plt.show()