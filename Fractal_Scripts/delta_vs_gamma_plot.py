import matplotlib.pyplot as plt
import math

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

def bin(s):
    t = s.split('.')
    return int(t[0], 2) + int(t[1], 2) / 2.**len(t[1])


c_1 = [[bin("0.11"), bin("0.11")], [bin("0.01"), bin("0.01")], [bin("0.1011"), bin("0.1111")], [bin("0.1001"), bin("0.0100")], [bin("0.1101"), bin("0.0010")], [bin("0.0101"), bin("0.0001")], [bin("0.100111"), bin("0.100111")], [bin("0.110001"), bin("0.010011")], [bin("0.011101"), bin("0.001001")], [bin("0.111011"), bin("0.111011")], [bin("0.001001"), bin("0.011101")], [bin("0.010011"), bin("0.110001")]]
plt.plot(chose_first(c_1), chose_second(c_1), 'k.')
plt.show()