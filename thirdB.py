import numpy.random as r
from libs import *


def genNormInInt(leftB, rightB, mean, disp):
    sample = r.normal(mean, (disp)**0.5)
    if (sample < rightB) & (sample > leftB):
        return sample
    return genNormInInt(leftB, rightB, mean, disp)


def genPoint():
    unif = r.uniform(0,1)
    w1 = 0.21
    w2 = 0.68
    if unif < w1:
        return -abs(r.standard_cauchy())
    elif unif < w1 + w2:
        return genNormInInt(0, 4, 2, 4)
    else:
        return (abs(r.standard_cauchy()))**0.5 + 4


def genSample(size = 1):
    rez = []
    for i in range(size):
        rez.append(genPoint())
    return rez


map = {
    "mean":"Среднее арифметическое",
    "hodges":"Ходжеса-Лемана",
    "pirson":"Пирсона-Тьюки",
    "absoluteDamage":"Модуль отклонения",
    "quadrDamage":"Квадратичный риск",
    "strangeDamage":"Дельта=0.1 риск"
}

N = 20
oldN = N
rez = {
    "mean":{"quadrDamage":[0 for x in range(0,4)],"absoluteDamage":[0 for x in range(0,4)],"strangeDamage":[0 for x in range(0,4)]},
    "hodges":{"quadrDamage":[0 for x in range(0,4)],"absoluteDamage":[0 for x in range(0,4)],"strangeDamage":[0 for x in range(0,4)]},
    "pirson":{"quadrDamage":[0 for x in range(0,4)],"absoluteDamage":[0 for x in range(0,4)],"strangeDamage":[0 for x in range(0,4)]}
}
for j in range(0,4):
    for i in range(0,50):
        sample = genSample(N)
        stat = mean(sample)
        rez["mean"]["quadrDamage"][j] += 1/50 * (quadrDamage(2,stat))
        rez["mean"]["absoluteDamage"][j] += 1/50 * (absoluteDamage(2,stat))
        rez["mean"]["strangeDamage"][j] += 1/50 * (strangeDamage(2,stat))
        stat = hodges(sample)
        rez["hodges"]["quadrDamage"][j] += 1/50 * (quadrDamage(2,stat))
        rez["hodges"]["absoluteDamage"][j] += 1/50 * (absoluteDamage(2,stat))
        rez["hodges"]["strangeDamage"][j] += 1/50 * (strangeDamage(2,stat))
        stat = pirson(sample)
        rez["pirson"]["quadrDamage"][j] += 1/50 * (quadrDamage(2,stat))
        rez["pirson"]["absoluteDamage"][j] += 1/50 * (absoluteDamage(2,stat))
        rez["pirson"]["strangeDamage"][j] += 1/50 * (strangeDamage(2,stat))
    N = N * 2

for statName in rez:
    statRez = rez[statName]
    for riskName in statRez:
        riskValues = statRez[riskName]
        points = []
        counter = 0
        for val in riskValues:
            points.append((oldN * 2**counter, val))
            counter += 1
        paramsExp = approximateExp(points)
        paramsPower = approximatePower(points)
        print(map[statName] + ", " + map[riskName] + ": ")
        print(points)
        if paramsExp[2] < paramsPower[2]:
            print(str(paramsExp[0]) + "*exp(-"+str(paramsExp[1])+"n), delta="+str(paramsExp[2]))
        else:
            print(str(paramsPower[0]) + "*n^(-"+str(paramsPower[1])+"), delta="+str(paramsPower[2]))

# print(rez)