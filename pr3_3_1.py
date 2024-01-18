import numpy as np

x = np.linspace(0,np.pi,100)
e= 0.9
tol = 1.e-10
roots = []
y=1.0
for i in range(len(x)) :
    a= x[i]
    while True :
        fy = y - e*np.sin(y) - a
        dfy = 1- e*np.cos(y)
        err = fy/dfy
        if np.abs(err) < tol : break
        y -= err
    roots.append(y)

print(roots)

