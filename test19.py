import numpy as np
import matplotlib.pyplot as plt
import cmath
# all roots soluved using by Muller Method

def Muller(p,x0,x1,x2,tol) :
    deg = len(p)-1
    while True :
        f0=np.polyval(p,x0)
        f1=np.polyval(p,x1)
        f2=np.polyval(p,x2)
        F10 = (f1-f0) /(x1-x0)
        F21 = (f2-f1)/(x2-x0)
        F210 = (F21-F10)/(x2-x0)
        a=F210
        b=F10 + F210*(x0-x1)
        c=f0
        xp = x0-(2*c/(b+cmath.sqrt(b**2-4*a*c)))
        xm = x0-(2*c/(b-cmath.sqrt(b**2-4*a*c)))
        if np.abs(np.polyval(p,xm)) < np.abs(np.polyval(p,xm)) :
            xnew = xm
        else:
            xnew = xp
        if np.abs(np.polyval(p,xnew)) < tol : break
        x2,x1,x0=x1,x0,xnew
    return xnew
a=[1,0,0,0,0,-3,-1]
deg = len(a) - 1
tol = 1.e-10
roots=[]

x0,x1,x2=1,2,3
for k in range(deg-2) :
    sol = Muller(a,x0,x1,x2,tol)
    roots.append(sol)
    b= np.zeros(len(a)-1,dtype=complex)
    b[0]=a[0]
    for i in range(1,len(b)):
        b[i]=a[i] + sol*b[i-1]
    a=b

solp = (-b[1]+cmath.sqrt(b[1]**2-4*b[0]*b[2]))/(2*b[0])
solm = (-b[1]-cmath.sqrt(b[1]**2-4*b[0]*b[2]))/(2*b[0])
roots.extend([solp,solm])

print(np.sort_complex(roots))
        
