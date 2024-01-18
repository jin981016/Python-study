import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr

"""
# fixed point iteration 
def gx(x) :
    fx = (3*x +1)**(1/4)
    return fx

tol = 1.e-6
x0=1

while True :
    x1 = gx(x0)
    if abs(x1 -x0) < tol :
        break
    x0 = x1

print(x1)
"""

coef = [1.,0.,0.,0.,0.,-3,-1]
x=1.0

dcoef = np.polyder(coef) #  (=np.arange(6,0,-1)*coef[0:-1])

deg = len(coef) - 1
tol = 1.e-10
roots=[]
for k in range(deg) :
    x=1.0
    while True :
        dlngdx =complex(0,1.e-20)
        for r in roots :
            dlngdx += 1/(x-r)
        fx = np.polyval(coef,x)
        dfx=np.polyval(dcoef,x)
        err = fx/(dfx - fx*dlngdx)
        if np.abs(err) < tol : break
        x= x-err
    roots.append(x)
print(np.sort_complex(roots))
