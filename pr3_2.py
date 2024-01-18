import numpy as np
import cmath

def P(x):
    y= ((2*h*c**2)/(x**5))/(np.exp(h*c/(x*k*T))-1) - 1e13
    return y
def Muller(x0,x1,x2,tol) :
    while True :
        f0 = P(x0)
        f1 = P(x1)
        f2 = P(x2)
        f10 = (f1-f0)/(x1-x0)
        f21 = (f2-f1)/(x2-x1)
        F210 = (f21-f10)/(x2-x0)
        a= F210
        b = f10 + F210*(x0-x1)
        c= f0
        xp = x0 -(2*c/(b+cmath.sqrt(b**2-4*a*c)))
        xm = x0 -(2*c/(b-cmath.sqrt(b**2-4*a*c)))
        if abs(P(xm)) < abs(P(xm)) :
            xnew = xm
        else:
            xnew = xp
        if np.abs(P(xnew)) < tol : break
        x2,x1,x0=x1,x0,xnew
    return xnew

tol=1.e-10
h=6.636e-34
c=2.989e8
k=1.381e-23
T=1e4
x0,x1,x2=0.e-9,1.e-5,1
roots=[]
for i in range(100):
    sol = Muller(x0,x1,x2,tol)
    roots.append(sol)
    b[0]=a[0]
    for i in range(1,3):
        b[i] = a[i] + sol*b[i-1]
    a=b
print(roots)

