import math

cycle = int(input("superstable cycle: "))
start_a = float(input("starting a:"))
trys = int(input("How many newton trys?"))

def cycles(a, start_x, iterations):
    y = a*math.sin(math.pi*start_x)
    for i in range(iterations):
        store.append(y)
        y = a * math.sin(math.pi * y)


for n in range(trys):
    store = []
    deriv = []
    double_deriv = []
    cycles(start_a,0.5,cycle)
    for m in range(cycle):
        if m == 0:
            deriv.append(math.pi*start_a*math.cos(math.pi*store[m]))
            double_deriv.append(math.pi * start_a * math.cos(math.pi * deriv[m]))
        else:
            deriv.append((math.pi*start_a*math.cos(math.pi*store[m]))*deriv[m-1])
            double_deriv.append((math.pi*start_a*math.cos(math.pi*deriv[m]))*double_deriv[m-1])
    if deriv[len(deriv)-1] == 0:
        print(deriv[len(deriv) - 1])
        break
    if abs(deriv[len(deriv) - 1]) > 5000 or math.isnan(double_deriv[len(double_deriv) - 1]):
        start_a -= 0.0001
        continue
    c = (deriv.pop())/double_deriv.pop()
    correction = 0.1/(0.1 + abs(c))
    start_a = start_a - (correction*c)

print(start_a)