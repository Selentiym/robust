import numpy.random as r
from math import *
# quantile = 0.511668
# success = 0
# successUn = 0
# counter = 0
# for test in range(100):
#     counter += 1
#     sum = 0
#     sumUn = 0
#     for i in range(3):
#         sum += r.exponential(1/3)
#         sumUn += r.uniform(0.1,0.4)
#     if sum >= quantile:
#         success += 1
#     if sumUn >= quantile:
#         successUn += 1
# print(success/counter)
# print(successUn/counter)


def g1(x):
    if x < log(2.7)/3:
        return 3*exp(-3*x)
    if x < 0.4:
        return 10/3
    return 3 * exp(-3 * x)


def g2(x):
    if x < log(27/5)/6:
        return 6*exp(-6*x)
    if x < 0.4:
        return 10/3
    return 6*exp(-6*x)


def g1red(x):
    if x > log(27/5)/6 and x < 0.4:
        return 0.129
    return g1(x)


def g2red(x):
    if x > log(27/5)/6 and x < 0.4:
        return 0.094
    return g2(x)


def decide(func):
    L1 = 0.0
    L2 = 0.0
    limit = log(1/0.2)
    for i in range(1, 10000):
        x = func()
        L1 += log(1.0/1.2) + log(g1(x)/g2(x))
        L2 += log(0.976/1.2) + log(g2(x)/g1(x))
        if L1 > limit:
            return 1, i
        if L2 > limit:
            return 2, i
    return 0, 100000


def decideRed(func):
    L1 = 0.0
    L2 = 0.0
    limit = log(1/0.2)
    for i in range(1, 10000):
        x = func()
        L1 += log(1.0/1.2) + log(g1red(x)/g2red(x))
        L2 += log(1.0/1.2) + log(g2red(x)/g1red(x))
        if L1 > limit:
            return 1, i
        if L2 > limit:
            return 2, i
    return 0, 100000000000


def genFirstHyp():
    return r.exponential(1/3)


def genSecondHyp():
    return r.exponential(1/6)


possibles = globals().copy()
possibles.update(locals())
h1 = possibles.get('genFirstHyp')
h2 = possibles.get('genSecondHyp')


for decideFunc in (possibles.get('decide'), possibles.get('decideRed')):
    risk1 = 0
    risk2 = 0
    succ1 = 0
    succ2 = 0
    j = 0
    for j in range(0, 100):
        rez, risk = decideFunc(h1)
        succ1 += int(rez == 1)
        risk1 += risk
        rez, risk = decideFunc(h2)
        succ2 += int(rez == 2)
        risk2 += risk

    print(succ1, risk1/100)
    print(succ2, risk2/100)
