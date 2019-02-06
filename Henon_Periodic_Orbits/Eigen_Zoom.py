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


def chose_first(elem):
    done = []
    for n in range(len(elem)):
        done.append(elem[n][0])
    return done


def chose_second(elem):
    done = []
    for n in range(len(elem)):
        done.append(elem[n][1])
    return done


points_to_plot = random_array([x_range[0], y_range[0]], [x_range[1], y_range[1]], number_of_points)
plt.plot(chose_first(points_to_plot), chose_second(points_to_plot), 'k,')
plt.show()
new_points_to_plot = []

for h in range(len(points_to_plot)):
    new_x, new_y = henon_attractor(1.4,0.3,points_to_plot[h][0],points_to_plot[h][1])
    new_points_to_plot.append([new_x, new_y])

plt.plot(chose_first(new_points_to_plot),chose_second(new_points_to_plot),'r,')
plt.show()
