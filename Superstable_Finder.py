cycle = int(input("superstable cycle: "))
start_a = float(input("starting a:"))
increment = float(input("increment: "))
accuracy = float(input("accuracy: "))
cycle_max = int(input("max cycle: "))
stop = False
temp = start_a
store = []
stay = True


def cycles(a, start_x, iterations):
    y = a*start_x*(1-start_x)
    for i in range(iterations):
        if i == (iterations-1):
            return y
        y = a*y*(1-y)


while cycle <= cycle_max:
    while stay:
        if temp >= 4.0:
            print("none found")
            break
        value = cycles(temp, 0.5, cycle)
        if abs(value - 0.5) < accuracy:
            if abs(cycles(temp, 0.5, int(cycle/2)) - 0.5) > accuracy:
                if len(store) > 0:
                    for m in range(len(store)):
                        if temp == store[m][1]:
                            break
                        elif m == len(store) - 1:
                            store.append([cycle, temp])
                            stop = True
                else:
                    store.append([cycle, temp])
                    break
            else:
                stop = False
        if stop:
            stop = False
            break
        else:
            temp += increment
    cycle *= 2
    stay = True

for c in range(len(store)):
    print(store[c][0])
    print(store[c][1])
    print(cycles(temp, 0.5, int(cycle)))
    print(abs(cycles(temp, 0.5, int(cycle/2)) - 0.5) > accuracy)
    print("")

