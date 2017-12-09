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


def genSmaple(size = 1):
    rez = []
    for i in range(size):
        rez.append(genPoint())
    return rez

N = 10
makeDuductions(genSmaple(N))
makeDuductions(genSmaple(N*2))
makeDuductions(genSmaple(N*4))

# for i in range(20):
#     print(r.standard_cauchy())