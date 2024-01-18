import numpy as np
import matplotlib.pyplot as plt
import sys

def codic(beta):
    n = 52
    gamma = np.arctan(2.**(-np.arange(n)))
    x=np.array([1.,0.])
    for i in range(n) :
        if beta <0 :
            siggma = -1
        else :
            siggma = +1
        beta -= siggma*gamma[i]
        factor = siggma*2.**(-i)
        R= np.array([[1,-factor],[factor,1]])
        R= R/np.sqrt(1+factor**2)
        x = R@x
    return x,beta
beta_deg =65.
beta_rad = np.deg2rad(beta_deg)
x,y=codic(beta_rad)
print(x[0]-np.cos(beta_rad) )
print(x[1]-np.sin(beta_rad) )
print(y)

