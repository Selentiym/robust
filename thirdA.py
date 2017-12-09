import numpy.random as r
from libs import *
sample = r.normal(2.0, 2.0, 10)
print(sample)
params = calcSampleParameters(sample)
print(params)
sigmaInt = (params[0] - (params[1])**0.5, params[0] + (params[1])**0.5)
print(sigmaInt)