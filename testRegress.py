import random as r
import libs
test = []
for i in range(1,10):
    # test.append((i,5.0*i**(-0.7) + (r.random()-0.5)*0))
    point = (i, 5.0*(2.71)**(-0.5*i) + (r.random()-0.5)/10000)
    test.append(point)
print(libs.approximateExp(test))
