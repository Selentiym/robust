import math
def calcSampleParameters(sample):
    sum = 0
    for el in sample:
        sum += el
    length = sample.__len__()
    if length == 0:
        length = 1
    mean = sum / length
    quadrSum = 0
    for el in sample:
        quadrSum += (el - mean)**2
    if (length < 2):
        disp = 0
    else:
        disp = quadrSum / (length - 1)
    return mean, disp, mean - disp ** 0.5, mean + disp ** 0.5


def makeDuductions(sample):
    params = calcSampleParameters(sample)
    print(sample)
    params = calcSampleParameters(sample)
    print("Выборочное среднее="+str(params[0])+", Выборочная дисперсия="+str(params[1]))
    if (params[2] < 2) & (params[3] > 2):
        print("Среднее 2 попало в доверительный интервал 3 сигма: "+(params[2], params[3]).__str__())
    else:
        print("СРЕДНЕЕ НЕ ПОПАЛО!!")


def mean(sample):
    sum = 0
    counter = 0
    for x in sample:
        sum += x
        counter += 1
    if counter > 0:
        return sum / counter
    else:
        return 0


def hodges(sample):
    newSample = []
    for (i,x) in enumerate(sample):
        for (j,y) in enumerate(sample):
            if (i > j):
                continue
            newSample.append(x/2+y/2)
    newSample.sort()
    ind = float(newSample.__len__())/2.0
    return newSample[int(math.floor(ind))]/2.0 + newSample[int(math.ceil(ind))]/2.0


def pirson(sample):
    sample.sort()
    n = sample.__len__()
    return (sample[int(n/16)]+sample[int(n/4)]+2*sample[int(n/2)]+sample[int(0.75*n)] + sample[int(15*n/16)])/6


def quadrDamage(x1,x2):
    return (x1 - x2)**2


def absoluteDamage(x1,x2):
    return abs(x1-x2)


def strangeDamage(x1,x2):
    temp = abs(x1-x2)
    if temp < 0.1:
        return 0.0
    return temp


def regress(points):
    sumX = 0
    sumY = 0
    sumXY = 0
    sumXX = 0
    n = points.__len__()
    if n == 0:
        return 0, 0
    for (x, y) in points:
        sumX += x
        sumY += y
        sumXY += x*y
        sumXX += x*x
    a = (n*sumXY - sumX*sumY)/(n*sumXX - sumX**2)
    b = (sumY - a * sumX) / n
    return a, b


def approximatePower(points):
    newPoints = [(math.log(x), math.log(y)) for (x, y) in points]
    (alpha, logA) = regress(newPoints)
    alpha = -alpha
    A = math.exp(logA)
    delta = 0
    for (n, y) in points:
        delta += (y - A*n**(-alpha))**2
    return A, alpha, delta


def approximateExp(points):
    newPoints = [(x, math.log(y)) for (x, y) in points]
    (alpha, logA) = regress(newPoints)
    alpha = -alpha
    A = math.exp(logA)
    delta = 0
    for (n, y) in points:
        delta += (y - A * math.exp(-alpha * n)) ** 2
    return A, alpha, delta
