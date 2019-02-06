import matplotlib.pyplot as plt
import random

eigenvalue = tuple(float(k) for k in input("eigenvalues x,y: ").split(', '))
x_range = tuple(float(i) for i in input("x range: ").split(', '))
y_range = tuple(float(j) for j in input("y range: ").split(', '))
number_of_points = int(input("number of points: "))


def random_array(min, max, length):
    list_of_points = []
    for m in range(length):
        random_point_x = random.uniform(min[0], max[0])
        random_point_y = random.uniform(min[1], max[1])
        list_of_points.append([random_point_x, random_point_y])

    return list_of_points

def henon_attractor(a, b, xx, yy):
    give_x = (yy + (a-(xx*xx)))
    give_y = (b*xx)
    return give_x, give_y