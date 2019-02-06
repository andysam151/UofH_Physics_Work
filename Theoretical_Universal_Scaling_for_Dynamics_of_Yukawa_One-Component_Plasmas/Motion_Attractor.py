"""
/// Theoretical Universal Scaling for the Dynamics of Yukawa One-Component Plasmas By: M. Andrew Sampson
/// This program maps the linear position and coulomb forces acting on a particle in a field of electrostatic waves.
/// the lambda, or l in this program represents the change in the electrostatic field. For l < 1, the field will
/// dissipate and form a strange attractor; This is what the program was designed to study.
/// the k value represents the strength of the electrostatic field. Since random noise develops at low k values, this
/// program is accurate only for k >> 1
"""
import matplotlib.pyplot as plt
import math
import time


# function for the system that defines the motion of the electron in the electrostatic field (Zaslavskii map)
def motion_attractor(l, k, x, d):
    # d represents the coulomb forces from other particles for k>>1 (neglecting neutral particles)
    give_d = l*d + k*math.sin((2*math.pi*x)%(2*math.pi))
    give_x = (x + give_d) % 1  # linear position of the particle
    return give_x, give_d


# parameters
l = float(input("lambda value:"))
k = float(input("k value:"))
iterations = int(input("points:"))

# initial conditions
x_initial = float(input("initial x:"))
y_initial = float(input("initial y:"))
time_out = int(input("time out in seconds:"))
box_length = float(input("size of box:"))

# instance variables
start_time = time.process_time()
x = [x_initial]
y = [y_initial]
y_range = [y_initial, y_initial]
x_range = [x_initial, x_initial]



for n in range(iterations):  # makes an array of the position,force pairs over the total iterations (discrete time)
    x_initial, y_initial = motion_attractor(l, k, x_initial, y_initial)
    x.append(x_initial)
    y.append(y_initial)

    if x_initial > x_range[1]:  # finds the minimum and maximum values for x and d to make an appropriately sized graph
        x_range[1] = x_initial
    if x_initial < x_range[0]:
        x_range[0] = x_initial
    if y_initial > y_range[1]:
        y_range[1] = y_initial
    if y_initial < y_range[0]:
        y_range[0] = y_initial

    if time.process_time() - start_time > time_out:  # quits loop if it takes too long
        print(len(x))
        print(time.process_time() - start_time)
        break

"""
/// Section 2
/// This section of the program is devoted to finding the fractal dimension (using the box method) of the attractor,
/// showing the progress of the program, and displaying the x vs d graph
"""
# progress variables
bool_25 = 0
bool_50 = 0
bool_75 = 0
count = 0  # tracks the number of boxes that have been checked for a given point
box_count = []

# finds the size of each box in calculating the fractal dimension
x_box = (abs(x_range[1]-x_range[0])/box_length)
y_box = (abs(y_range[1]-y_range[0])/box_length)

# makes sure the number boxes is an integer
if math.isinf(x_box) is False:
    if x_box - math.floor(x_box) != 0:
        x_box = math.floor(x_box) + 1
if math.isinf(y_box) is False:
    if y_box - math.floor(y_box) != 0:
        y_box = math.floor(y_box) + 1

crunch_time = time.process_time()

for m in range(len(x)):  # loops through each point
    # progress markers
    if m > (len(x)/4) and bool_25 is not True:
        print("25% done")
        bool_25 = True
    if m > (len(x)/2) and bool_50 is not True:
        print("50% done")
        bool_50 = True
    if m > (3 * len(x)/4) and bool_75 is not True:
        print("75% done")
        bool_75 = True

    # finds which box the point fits in and counts the box if it hasn't been used already
    for z in range(int(x_box )+ 1):  # loops through columns of boxes
        # checks if the point is in the x range of the box
        if x[m] >= (x_range[0] + box_length * z) and x[m] <= (x_range[0] + box_length * (z + 1)):
            for q in range(int(y_box) + 1):  # loops through rows of boxes in the column
                if time.process_time() - crunch_time > time_out:  # quits loop if it takes too long
                    break
                # checks if the point is in the y range of the box
                if y[m] >= (y_range[0] + box_length * q) and y[m] <= (y_range[0] + box_length * (q + 1)):
                    if len(box_count) == 0:  # adds first box
                        box_count.append((z, q))
                    else:
                        for s in range(len(box_count)):  # loops through boxes with known points in them
                            if box_count[s] == (z, q):  # checks if the point falls in taken box s
                                break
                            elif count + 2 < len(box_count):  # checks if all of the known boxes have been checked
                                count += 1
                            else:  # adds the box if the other checks aren't true
                                box_count.append((z, q))
                                break
                count = 0
        if time.process_time() - crunch_time > time_out:  # quits loop if it takes too long
            break
    if time.process_time() - crunch_time > time_out:  # quits loop if it takes too long
        break

dimension = -1 * math.log(len(box_count), box_length)  # calculates the fractal dimension

# prints all of the values found
print("number of boxes: " + str(len(box_count)) + " box edge length is " + str(box_length))
print("dimension is: " + str(dimension))
print("Finished in " + str(time.process_time()) + "seconds")

# makes the x vs d graph
plt.plot(x, y, 'k,')
plt.show()
