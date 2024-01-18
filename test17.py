import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
import cmath
def f(x):
    y = x**4-3*x-1
    return y

def ND(x1,x2) :
    f_x1x2 = (f(x2) - f(x1))/(x2-x1)
    return f_x1x2
def NDD(x1,x2,x3) :
    f_x1x3 = (ND(x3,x2) - ND(x2,x1))/(x3-x1)
    return f_x1x3

x0,x1,x2 = 0.0,0.5,1.0
tol = 1.e-10
while True :
    f0 = f(x0)
    f1= f(x1)
    f2= f(x2)
    
   # f10 = (f1-f0)/(x1-x0)
   # F210 =((f2-f1)/(x2-x1)-f10)/(x2-x0)
    f10 , f21 = ND(x0,x1) , ND(x1,x2)
    F210=NDD(x0,x1,x2)
    a= F210
    b=f10 +F210*(x0-x1)
    c=f0
    xp = x0 - ((2*c) / (b+cmath.sqrt(b**2-4*a*c)))
    xm = x0 -((2*c)/(b-cmath.sqrt(b**2-4*a*c)))
    if abs(f(xm)) < abs(f(xm)) :
        xnew = xm
    else :
        xnew = xp
    if abs(xnew-x1) < tol :break
    x0=x1
    x1=x2
    x2=xnew

print(xnew)
