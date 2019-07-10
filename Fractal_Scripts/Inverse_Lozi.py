import matplotlib.pyplot as plt

points = int(input("points: "))
a = float(input("a: "))
b = float(input("b: "))
eigen_neighborhood = float(input("eigen neighborhood distance: "))

eigen = [1,0]
x_iter = a/(1-b+a)

if x_iter < 0:
    x_iter = a/(1-b-a)

y_iter = b*x_iter
eigen[1] = (a + (b*pow(pow(a/b,2) + (4/b),0.5)))/2

if y_iter < 0:
    eigen[1] = (-a + (b * pow(pow(a / b, 2) + (4 / b), 0.5))) / 2

temp_a = pow(1/(1+pow(eigen[1],2)),0.5)
eigen = [eigen_neighborhood*temp_a, eigen_neighborhood*temp_a*eigen[1]]
x_iter += eigen[0]
y_iter += eigen[1]

x = [x_iter]
y = [y_iter]

def inverse_lozi_attractor(a,b,x,y):
    give_x = y/b
    give_y = x + a*(abs(y/b) - 1)
    return give_x, give_y

for i in range(points):
    x_iter, y_iter = inverse_lozi_attractor(a,b,x_iter,y_iter)
    x.append(x_iter)
    y.append(y_iter)

plt.plot(x,y,'k,')
plt.show()