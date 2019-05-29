import math

eigen = []
d = float(input("starting d: "))
iterations = int(input("newton iterations: "))
numValues = int(input("number of eigenvalues: "))

for n in range(numValues):
    current = float(input("Value " + str(n+1) + ": "))
    power = int(input("Power: "))
    eigen.append([current, power])

for m in range(iterations):
    deriv = 0
    fxn = -1
    for k in range(len(eigen)):
        fxn += pow(pow(eigen[k][0], eigen[k][1]), d)
        deriv += pow(pow(eigen[k][0], eigen[k][1]), d) * math.log(abs(pow(eigen[k][0], eigen[k][1])))
    d -= fxn/deriv

print(d)