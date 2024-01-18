import numpy as np
import math


coef = [1/5,0,np.log(0.1),np.sqrt(2)]

dcoef = np.polyder(coef)
deg = len(coef) - 1
roots=[]
tol = 1.e-6
for i in range(deg) :
    x= 1.0
    while True :
        dlndx = 1.e-20
        for r in roots :
            dlndx += 1/(x-r)
        fx = np.polyval(coef,x)
        dfx=np.polyval(dcoef,x)
        err = fx/(dfx - fx*dlndx)
        if np.abs(err) < tol : break
        x= x-err
    if x < 0 :
        x= 'null'
    roots.append(x)
rt=[]
for i in range (len(roots)) :
    if roots[i] != 'null':
        x= roots[i]**2
        rt.append(round(x,6))

print(rt)

        


