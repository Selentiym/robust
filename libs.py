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
