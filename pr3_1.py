import numpy as np
import cmath
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


"""
def func(x):
    y = (2*h*c**2/(x**5))/(np.exp(h*c/(x*k*T))-1) - 1.e13
    return y

h= 6.626e-34
c=2.998e8
k = 1.381e-23

T=1e4


roots=[]
for i in np.arange(0,2):
    root = fsolve(func,i,xtol=1.e-10)
    a= float(root)
    roots.append(a)

print(set(roots))
"""



n=100
roots=[]
for i in range(n):
    x=5
    while True :
        dlngx = 1e-3
        for r in roots :
            dlngx += 1/(x-r)
        fx = func(x) - 0.1
        dfx = ((0.5)**(0.5)*x**(-3/2) - 1/5) * func(x)
        err = fx/(dfx - fx*dlngx)
        if np.abs(err)< tol: break
        x = x- err
    roots.append(x)
print(roots)

"""
def Planck(x):
    y = (2*h*c**2/(x**5))/(np.exp(h*c/(x*k*T))-1) - 1e13
    return y
h= 6.626e-34
c=2.998e8
k = 1.381e-23

T=1e4

x0,x1=10,1000
tol = 1e-10
pfc = 0
f0 = Planck(x0)
f1 = Planck(x1)
while True :
    c= (x0*f1 - x1*f0)/(f1-f0)
    if abs(c-x0) < tol : break
    fc = Planck(c)
    if f0*fc < 0 :
        x1 = c
        f1= Planck(x1)
        if fc*pfc > 0 :f0 = 0.5*f0
    else :
        x0 = c
        f0 =Planck(x0)
        if fc*pfc > 0 : f1=0.5*f1
    pfc = fc
print(c,Planck(c))
        


print(x)
"""    
