"""
/// Theoretical Universal Scaling for the Dynamics of Yukawa One-Component Plasmas By: M. Andrew Sampson
/// This program maps the logistic map of a particle in a field of electrostatic waves.
/// the lambda, or l in this program represents the change in the electrostatic field. For l < 1, the field will
/// dissipate and form a strange attractor; This is what the program was designed to study.
/// the k value represents the strength of the electrostatic field. Since random noise develops at low k values, this
/// program is accurate only for k >> 1
"""

import matplotlib.pyplot as plt
import random
import math


# function for the system that defines the motion of the electron in the electrostatic field (Zaslavskii map)
def motion_attractor(l, k, x, d, loops):
    # d represents the coulomb forces from other particles for k>>1 (neglecting neutral particles)
    give_d = l*d + k*math.sin((2*math.pi*x) % (2*math.pi))
    give_x = (x + give_d) % 1  # linear position of the particle
    for i in range(loops):
        if i == (loops-1):
            cycle_x.append(give_x)
            cycle_y.append(give_d)
        give_d = l * give_d + k * math.sin((2 * math.pi * give_x) % (2 * math.pi))
        give_x = (give_x + give_d) % 1


# parameters
start_k = float(input("Starting k: "))
stop_k = float(input("Ending k: "))
increment = float(input("increment: "))
num_try = int(input("number of points to try: "))
trys = int(input("iterations per point: "))
accuracy = float(input("accuracy margin: "))

# instance variables
cycle_x = []
cycle_y = []
final_y = []
k_values = []
two_cycles = []

#loops through values of k from the start k to the end k with steps of size increment
for n in range(int(start_k/increment), int(stop_k/increment)):
    m = increment * n
    attractors = []
    cycle_x = []
    for b in range(0, num_try):  # loops through random points
        point_x = random.uniform(0, 1)
        point_y = random.uniform(0, 1)
        motion_attractor(0.1, m, point_x, point_y, trys)
        if len(attractors) > 0:
            for g in range(len(attractors)):
                if abs(attractors[g][0]-cycle_x[b]) <= accuracy and abs(attractors[g][1]-cycle_y[b]) <= accuracy:
                    break
                elif g == (len(attractors)-1):
                    attractors.append([cycle_x[b], cycle_y[b]])
                    break
        elif b == 0:
            attractors.append([cycle_x[0], cycle_y[0]])
    for c in range(len(attractors)):
        final_y.append(attractors[c][0])
        k_values.append(m)
        if len(attractors) == 2:
            two_cycles.append([k_values[len(k_values)-1], final_y[len(final_y)-1]])


print(two_cycles)
plt.plot(k_values, final_y, 'k,')
plt.show()
