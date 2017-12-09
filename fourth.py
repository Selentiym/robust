import numpy.random as r
quantile = 0.511668
success = 0
successUn = 0
counter = 0
for test in range(100):
    counter += 1
    sum = 0
    sumUn = 0
    for i in range(3):
        sum += r.exponential(1/3)
        sumUn += r.uniform(0.1,0.4)
    if sum >= quantile:
        success += 1
    if sumUn >= quantile:
        successUn += 1
print(success/counter)
print(successUn/counter)
