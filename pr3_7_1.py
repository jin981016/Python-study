import numpy as np

tol = 1.e-6

coef = np.array([46189,0,-109395,0,90090,0,-30030,0,3465,0,-63],dtype=float)*(1/256) 
dcoef = np.polyder(coef)
deg = len(coef)-1
print(deg)
roots=[]
for i in range(deg):
    x= 5.0
    while True:
        dlndx = 0
        for r in roots :
            dlndx += 1/(x-r)
        fx = np.polyval(coef,x)
        dfx = np.polyval(dcoef,x)
        err = fx/(dfx-fx*dlndx)
        if abs(err) < tol : break
        x -= err
    roots.append(round(x,6))
    
print(roots,len(roots))
