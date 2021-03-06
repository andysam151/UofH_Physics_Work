import matplotlib.pyplot as plt
import time
import math

def henon_attractor(a, b, x, y):
    give_x = y + a*(1-abs(x))
    give_y = b*x
    return give_x, give_y


# dependant conditions
a = float(input("a value:"))
b = float(input("b value:"))
iterations = int(input("points:"))

# initial conditions
x_initial = float(input("initial x:"))
y_initial = float(input("initial y:"))
time_out = int(input("time out in seconds:"))
box_length = float(input("size of box:"))
start_time = time.process_time()
x = [x_initial]
y = [y_initial]
y_range = [y_initial, y_initial]
x_range = [x_initial, x_initial]


for n in range(iterations):
    x_initial, y_initial = henon_attractor(a, b, x_initial, y_initial)
    x.append(x_initial)
    y.append(y_initial)
    if x_initial > x_range[1]:
        x_range[1] = x_initial
    if x_initial < x_range[0]:
        x_range[0] = x_initial
    if y_initial > y_range[1]:
        y_range[1] = y_initial
    if y_initial < y_range[0]:
        y_range[0] = y_initial
    if time.process_time() - start_time > time_out:
        print(len(x))
        print(time.process_time() - start_time)
        break

bool_25 = 0
bool_50 = 0
bool_75 = 0
count = 0
box_count = []
x_box = (abs(x_range[1]-x_range[0])/box_length)
y_box = (abs(y_range[1]-y_range[0])/box_length)

if x_box - int(x_box) != 0:
    x_box = int(x_box) + 1
if y_box - int(y_box) != 0:
    y_box = int(y_box) + 1

crunch_time = time.process_time()

for m in range(len(x)):
    if m > (len(x)/4) and bool_25 is not True:
        print("25% done")
        bool_25 = True
    if m > (len(x)/2) and bool_50 is not True:
        print("50% done")
        bool_50 = True
    if m > (3 * len(x)/4) and bool_75 is not True:
        print("75% done")
        bool_75 = True
    for z in range(x_box + 1):
        if x[m] >= (x_range[0] + box_length * z) and x[m] <= (x_range[0] + box_length * (z + 1)):
            for q in range(y_box + 1):
                if time.process_time() - crunch_time > time_out:
                    break
                if y[m] >= (y_range[0] + box_length * q) and y[m] <= (y_range[0] + box_length * (q + 1)):
                    if len(box_count) == 0:
                        box_count.append((z, q))
                    else:
                        for s in range(len(box_count)):
                            if box_count[s] == (z, q):
                                break
                            elif count + 2 < len(box_count):
                                count += 1
                            else:
                                box_count.append((z, q))
                                break
                count = 0
        if time.process_time() - crunch_time > time_out:
            break
    if time.process_time() - crunch_time > time_out:
        break
dimension = -1 * math.log(len(box_count), box_length)
print("number of boxes: " + str(len(box_count)) + " number of boxes: " + str(x_box*y_box))
print("dimension is: " + str(dimension))
print("Finished in " + str(time.process_time()) + "seconds")

plt.plot(x,y,'k,')
plt.show()
