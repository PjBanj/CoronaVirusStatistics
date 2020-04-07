import numpy
import pylab as p
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math

def logGrowth(x, a, b, c):
    return a*numpy.exp(b*x)+c

def func(t,a,b):
    return a+b*numpy.log(t)
	

days = numpy.empty(32)
b = numpy.arange(1, 33)
ind = numpy.arange(len(days))
numpy.put(days, ind, b)

xValues=numpy.array([1,2,3,4,5,6,7, 8,9, 10, 11, 12, 13, 14 , 15, 16, 17, 18, 19, 20, 21 , 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])
yValues = numpy.array([60846, 75698, 93842, 112470, 130478, 151980, 179446, 203788, 234768, 258214])
totalCases = numpy.array([53, 80, 98, 164, 214, 279, 423, 647, 937, 1215, 1629, 1896, 2234, 3487, 4226, 7038, 10442, 15219, 18747, 24583, 33404,	44183, 54453, 68440, 85356, 103321, 122653,	140904,	163539,	186101,	213144,	239279])
print(totalCases.size)
print(xValues.size)
#totalCases = numpy.array([1, 1,	2,	2,	5,	5,	5,	5,	5,	7,	8,	8,	11,	11,	11,	11,	11,	11,	11,	11,	12,	12,	13,	13,	13,	13,	13,	13,	13,	13,	15,	15,	15,	15,	15,	15,	16,	16,	24,	30,	53,	80,	98,	164,	214,	279,	423,	647,	937,	1215,	1629,	1896,	2234,	3487,	4226,	7038,	10442,	15219,	18747,	24583,	33404,	44183,	54453,	68440,	85356,	103321,	122653,	140904,	163539,	186101,	213144,	239279])


print(xValues)
print(totalCases)

zValues=numpy.array([838,1102,1428,1876,2314, 2793, 3539, 4503, 5586, 6600])
p0 = numpy.random.exponential(size=3)
bounds = (0, [50000., 3., 1000000000.])
#(a,b,c,),cov = opt.curve_fit(logGrowth, xValues, yValues, bounds=bounds, p0=p0)
popt, pcov = opt.curve_fit(logGrowth, xValues, totalCases, maxfev=100000)
plt.scatter(xValues, totalCases)
print(*popt)
plt.plot(xValues, logGrowth(xValues, *popt))
plt.title('Logistic Curve Fitting vs Real Data of CoronaVirus in US')
plt.legend(['Logistic Model', 'Real data'])
plt.xlabel('March 2nd to April 2nd in Days')
plt.ylabel('Cases')
plt.show();

 
 
 