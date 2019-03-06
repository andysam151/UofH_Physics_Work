import math

trys = int(input("newton iterations: "))
d = float(input("initial d: "))
num_epsilon = int(input("number of values: "))
values = []

for i in range(num_epsilon):
    new_val = float(input("value " + str(i+1) + ": "))
    values.append(new_val)

for j in range(trys):
    top = -1
    for k in range(len(values)):
        top += pow(values[k], d)

    bottom = 0
    for m in range(len(values)):
        bottom += pow(values[m], d) * math.log(abs(values[m]))

    c = top/bottom
    d = d - (c*(.001/(.001+abs(c))))

print(d)
