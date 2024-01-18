import numpy as np

k = 1.381e-23
c=2.998e8
h=6.626e-34
T= 1e4

B = 1e13
tol= 1.e-10

a = (h*c)/(k*T)
b = (2*h*c*c)/(B)
b= b**(-1)

roots = []
rt = []


for i in range (4):
    x=1.0
    while True :
        dlndx = 0
        for r in roots:
            dlndx += 1/(x-r)
        fx = b*x**5 *(np.exp(a/x) - 1) -1
        dfx = b*x**3*(np.exp(a/x) - 1)*(5*x-a)
        err = fx / (dfx-fx*dlndx)
        if np.abs(err)< tol :
            break
        x -= err
    
    roots.append(x)
    y= roots[i]
    if y > 0 :
        rt.append(y)
    if len(rt) == 2 : break
print(rt)
