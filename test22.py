import numpy as np
from scipy import integrate




def func(x):
    y = np.exp(x)
    return y
# using numpy 
"""
def Trap(F,a,b,n) :
    h = (b-a) / float(n)
    total = 0 
    for j in range(1,n) :
        t = F(a+j*h)
        total += t
    y = h*(0.5*(F(a)+F(b))+total)
    return y

a,b = 0 , 1
perr = 1


for i in range(0,11) :
    n= 2**i
    sol = Trap(func,a,b,n)
    fx = (np.exp(1) - 1.0)
    err = abs(fx -sol)
    ratio = perr/err
    perr = err
    print(f"{n:3d}  {sol:.6f}  {err:.4e}  {ratio:.2f} ")
"""  
# using scipy

a,b = 0,1
for j in range(11):
    n = 2**j
    x = np.linspace(a,b,n+1)
    y = func(x)
    sol = integrate.trapz(y,x)
    err = abs(np.exp(1) -1. - sol)
    print(sol,err)
