import matplotlib.pyplot as plt
import random

orbits = int(input("orbits: "))
points = int(input("points per orbit: "))
a = float(input("a: "))
b = float(input("b: "))
count_x = 0
count_y = 0
binary_string_x = ""
gamma = []
delta = []

def bin(s):
    t = s.split('.')
    return int(t[0], 2) + int(t[1], 2) / 2.**len(t[1])

def lozi_attractor(a,b,x,y):
    give_x = y + a*(1-abs(x))
    give_y = b*x
    return give_x, give_y

for q in range(orbits):
    count_x = 0
    count_y = 0
    binary_string_x = ""
    x_iter = random.random()
    y_iter = random.random()
    x = [x_iter]
    y = [y_iter]

    for i in range(points):
        x_iter, y_iter = lozi_attractor(a,b,x_iter,y_iter)
        x.append(x_iter)
        y.append(y_iter)

    for j in range(len(x)-1):
        if x[j+1] > 0:
            count_x = (count_x + 1)%2

        if x[j] < 0:
            count_y = (count_y + 1)%2

        if(len(delta) > 0):
            if count_y < 1:
                temp_del = (-1*(delta[-1]-1))/10
                delta.append(1-((count_y/2)+temp_del))
            else:
                temp_del = "0."
                temp_count_y = count_y
                if j < 15:
                    for u in range(j):
                        temp_del += str(temp_count_y)
                        if x[j-u] < 0:
                            temp_count_y = (temp_count_y + 1) % 2
                else:
                    for u in range(14):
                        temp_del += str(temp_count_y)
                        if x[j-u] < 0:
                            temp_count_y = (temp_count_y + 1) % 2
                try:
                    delta.append(bin(temp_del))
                except OverflowError:
                    delta.append(delta[-1])
        else:
            delta.append(1-(count_y/2))

        binary_string_x += str(count_x)

        try:
            gamma.append(bin("0."+binary_string_x[::-1]))
        except OverflowError:
            gamma.append(gamma[-1])

plt.plot(gamma,delta,'k,')
plt.show()