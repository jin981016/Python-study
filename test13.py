import numpy as np
import matplotlib.pyplot as plt
import sys

def FiniteDifference(F,x,h) :
    fdf = (F(x+h) - F(x))/ h
    bdf = (F(x)-F(x-h))/ h
    cdf = (F(x+h)-F(x-h))/(2*h)
    return fdf, bdf, cdf

def function(x):
    return np.exp(x)

h= np.logspace(-15,0,200)
fdf,bdf,cdf = FiniteDifference(function,1,h)
ferr=np.abs(fdf -np.exp(1))
berr=np.abs(bdf -np.exp(1))
cerr=np.abs(cdf -np.exp(1))

fig = plt.figure(1,figsize=(7,5))
plt.plot(h,ferr,label='forward')
plt.plot(h,berr,label='backward')
plt.plot(h,cerr,label='central')

plt.xlim(1,1.e-15)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('h')
plt.ylabel('error')
plt.legend()
plt.show()
