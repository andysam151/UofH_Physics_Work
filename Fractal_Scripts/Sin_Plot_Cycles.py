import time
import math

accuracy = float(input("accuracy: "))
lines = int(input("number of x/y grid lines?"))
cycle_range = [int(input("Starting cycle: ")), int(input("Ending cycle: "))]
timeout = int(input("timeout (s): "))

start_time = time.process_time()
y_range = [-1, 1]
x_range = [0, 1]
cycle_store = []
f = open("Quadratic_Cycle_Values.txt", "w+")

def chose_third(elem):
    return elem[2]


def cycle_attractor(xx, yy, cycle):
    start_x = xx
    start_y = yy
    for n in range(cycle):
        try:
            start_x = start_y
            start_y = (2*math.cos(math.pi*start_x/2.0))-1
        except OverflowError:
            return False

    if abs(xx - start_x) < accuracy and abs(yy - start_y) < accuracy:
        return True
    return False

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
            if cycle_attractor(x, y, s):
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
