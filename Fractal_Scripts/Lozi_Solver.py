x_range = tuple(float(x_input.strip()) for x_input in input("coordonates: ").split(","))
cycle = int(input("cycles: "))

def lozi_attractor(a,b,x,y):
    give_x = y + a*(1-abs(x))
    give_y = b*x
    return [give_x, give_y]

for n in range(cycle):
    print(lozi_attractor(1.7, 0.5, x_range[0], x_range[1]))
    x_range = lozi_attractor(1.7, 0.5, x_range[0], x_range[1])