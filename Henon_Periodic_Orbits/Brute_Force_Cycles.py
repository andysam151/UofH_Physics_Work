import time

a = float(input("a: "))
b = float(input("b: "))
x_initial = float(input("Seed x: "))
y_initial = float(input("Seed y: "))
iterations = int(input("Seed iterations: "))
accuracy = float(input("accuracy: "))
lines = int(input("number of x/y grid lines?"))
cycle_range = [int(input("Starting cycle: ")), int(input("Ending cycle: "))]
timeout = int(input("timeout (s): "))

start_time = time.process_time()
y_range = [y_initial, y_initial]
x_range = [x_initial, x_initial]
cycle_store = []
f = open("Cycle_Values.txt", "w+")

def chose_third(elem):
    return elem[2]


def henon_attractor(a, b, xx, yy):
    give_x = (yy + (a-(xx*xx)))
    give_y = (b*xx)
    return give_x, give_y


def cycle_attractor(a, b, xx, yy, cycle):
    start_x = xx
    start_y = yy
    for n in range(cycle):
        try:
            temp = start_x
            start_x = start_y + a - (start_x**2)
            start_y = b * temp
        except OverflowError:
            return False

    if abs(xx - start_x) < accuracy and abs(yy - start_y) < accuracy:
        return True
    return False


for n in range(iterations):
    x_initial, y_initial = henon_attractor(a, b, x_initial, y_initial)
    if x_initial > x_range[1]:
        x_range[1] = x_initial
    if x_initial < x_range[0]:
        x_range[0] = x_initial
    if y_initial > y_range[1]:
        y_range[1] = y_initial
    if y_initial < y_range[0]:
        y_range[0] = y_initial
    if time.process_time() - start_time > timeout:
        print(time.process_time() - start_time)
        break

for j in range(lines):
    for c in range(lines):
        done = False
        x = x_range[0] + ((x_range[1]-x_range[0])/lines)*j
        y = y_range[0] + ((y_range[1] - y_range[0]) / lines) * c
        if len(cycle_store) > 0:
            for g in range(len(cycle_store)):
                if abs(cycle_store[g][0] - x) < 0.01 and abs(cycle_store[g][1] - y) < 0.01:
                    done = True
                    break
        if done:
            continue
        for s in range(cycle_range[0],cycle_range[1]):
            if cycle_attractor(a, b, x, y, s):
                cycle_store.append((x, y, s))
                break
            if time.process_time() - start_time > timeout:
                print(time.process_time() - start_time)
                break

cycle_store.sort(key=chose_third)

for h in range(len(cycle_store)):
    if h == 0:
        f.write('{}'.format(cycle_store[h][2]) + " Cycle: (" + '{}'.format(cycle_store[h][0]) + ", " + '{}'.format(cycle_store[h][1]) + ")\n")
    elif cycle_store[h][2] == cycle_store[h-1][2]:
        f.write('{}'.format(cycle_store[h][2]) + " Cycle: (" + '{}'.format(cycle_store[h][0]) + ", " + '{}'.format(cycle_store[h][1]) + ")\n")
    else:
        f.write("\n")
        f.write('{}'.format(cycle_store[h][2]) + " Cycle: (" + '{}'.format(cycle_store[h][0]) + ", " + '{}'.format(cycle_store[h][1]) + ")\n")

f.close()
