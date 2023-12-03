import matplotlib.pyplot as plot
import numpy

x = [29,28,34,31,25]
y = [77,62,93,84,59]

xbar = numpy.average(x)
ybar = numpy.average(y)

Sxx = 0
Sxy = 0

for i in range(len(x)):
    Sxx += (x[i]-xbar)**2
    # print(Sxx)

    Sxy += (x[i]-xbar)*(y[i]-ybar)
    # print(Sxy)
    # print(f"i = {i}")

a = Sxy/Sxx

b = ybar-xbar*a

# print(b)

newY = [] 

for j in x:
    newY.append(a*j+b)
    # print(f"j = {y[i]}")

print(newY)

plot.scatter(x,y)
plot.plot(x,newY)
plot.show()

