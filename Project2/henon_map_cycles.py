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
    det = 0
    store = []
    d_xx = []
    d_xy = []
    d_yx = []
    d_yy = []
    x_c = []
    y_c = []
    cycles(a,b,start_x,start_y,cycle)
    for m in range(cycle):
        if m == 0:
            d_xx.append(-2*store[m][0])
            d_xy.append(1)
            d_yx.append(b)
            d_yx.append(0)

        else:
            d_xx.append((-2 * store[m][0] * d_xx[-1])+(b*d_yx[-1]))
            d_xy.append((-2 * store[m][0] * d_xy[-1])+(b*d_yy[-1]))
            d_yx.append(d_xx[-1])
            d_yx.append(d_xy[-1])
    det = 1 / ((d_xx*d_yy)-(d_xy*d_yx))
    d_xx.append(det * d_yy[-1])
    d_xy.append(det * -1 * d_xy[-1])
    d_yx.append(det * -1 * d_yx[-1])
    d_yx.append(det * d_xx[-2])
    x_c = (store[m][0]-start_x) * (1/deriv_y[len(deriv_y)-1])
    y_c = (store[m][1]-start_y) * ((1/(b*deriv_x[len(deriv_x)-1]))+(((2*store[m][0]*deriv_x[len(deriv_x)-1])-(b*deriv_x[len(deriv_x)-2]))/(b*deriv_y[len(deriv_y)-1]*deriv_x[len(deriv_x)-1])))
    x_correction = 0.01/(0.01 + abs(x_c))
    y_correction = 0.01/(0.01 + abs(y_c))
    start_x = start_x - (x_correction*x_c)
    start_y = start_y - (y_correction * y_c)

print(start_x)
print(start_y)

temp = start_x
start_x = (start_y + (a - (start_x ** 2)))
start_y = (b * temp)

print(start_x)
print(start_y)
