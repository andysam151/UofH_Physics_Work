a = float(input("a value:"))
b = float(input("b value:"))
start_x = float(input("start x: "))
start_y = float(input("start y: "))
cycle = int(input("stable cycle: "))
trys = int(input("How many newton trys?"))


def cycles(a,b, start_x, start_y, iterations):
    give_x = (start_y + (a-(start_x*start_x)))
    give_y = (b*start_x)
    for n in range(iterations):
        temp = give_x
        store.append([give_x,give_y])
        give_x = (give_y + (a - (give_x * give_x)))
        give_y = (b * temp)


for n in range(trys):
    store = [[start_x, start_y]]
    d_xx = []
    d_xy = []
    d_yx = []
    d_yy = []
    cycles(a,b,start_x,start_y,cycle)
    d_xx.append(1.0)
    d_xy.append(0)
    d_yx.append(0)
    d_yy.append(1.0)
    for m in range(cycle):
        d_xx.append((-2.0 * store[m][0] * d_xx[-1])+(d_yx[-1]))
        d_xy.append((-2.0 * store[m][0] * d_xy[-1])+(d_yy[-1]))
        d_yx.append(b*d_xx[-2])
        d_yy.append(b*d_xy[-2])
        if m == cycle - 1:
            d_xx.append(d_xx[-1]-1)
            d_xy.append(d_xy[-1])
            d_yx.append(d_yx[-1])
            d_yy.append(d_yy[-1] - 1)
            if ((d_xx[-1] * d_yy[-1]) - (d_xy[-1] * d_yx[-1])) != 0:
                det = 1.0 / ((d_xx[-1] * d_yy[-1]) - (d_xy[-1] * d_yx[-1]))
                d_xx.append(det * d_yy[-1])
                d_xy.append(det * -1.0 * d_xy[-1])
                d_yx.append(det * -1.0 * d_yx[-1])
                d_yy.append(det * d_xx[-2])
                x_c = (store[m+1][0] - start_x) * (d_xx[-1]) + (store[m+1][1] - start_y) * (d_xy[-1])
                y_c = ((store[m+1][0] - start_x) * (d_yx[-1])) + ((store[m+1][1] - start_y) * (d_yy[-1]))
                x_correction = 0.0001 / (0.0001 + abs(x_c))
                y_correction = 0.0001 / (0.0001 + abs(y_c))
                start_x = start_x - (x_correction * x_c)
                start_y = start_y - (y_correction * y_c)
            else:
                break

print(start_x)
print(start_y)
