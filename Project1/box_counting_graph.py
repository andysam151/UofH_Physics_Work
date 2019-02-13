import matplotlib.pyplot as plt
import math
from scipy.stats import linregress


def chose_first(elem):
    done = []
    for n in range(len(elem)):
        done.append(math.log(elem[n][0]))
    return done


def chose_second(elem):
    done = []
    for n in range(len(elem)):
        done.append(math.log(elem[n][1]))
    return done


c_1 = [[0.01, 2065], [0.01, 2111], [0.005, 4770], [0.005, 4895], [0.0025, 10081], [0.0025, 10978], [0.00125, 18543], [0.00125, 23370], [0.00125, 26570]]
print(linregress(chose_first(c_1), chose_second(c_1)))
plt.plot(chose_first(c_1), chose_second(c_1), 'k.')
plt.show()