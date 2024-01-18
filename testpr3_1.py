import numpy as np

coef=[0.5,1,0.9]
dcoef = np.polyder(coef)
deg =len(coef) - 1
print(dcoef)
roots=[]
tol=1.e-10
E=1.0
for i in range(deg):
    t= (-np.sqrt(2/E))-E/5
    while True :
        dlngx = complex(0,1e-20)
        for r in roots:
            dlngx += 1/(t-r)
        fx = np.polyval(coef,t)
        dfx=np.polyval(dcoef,t)
        err = fx/(dfx-fx*dlngx)

        if abs(err) < tol : break
        t = t- err
    roots.append((t))

print(roots)


sol=[]
for i in range(len(roots)):
    E0,E1 = 1,5
    while True:
        f0= (roots[i] - ((-(2/E0)**(0.5))-E0/5))
        f1= (roots[i] - ((-(2/E1)**(0.5))-E1/5))
        E2 = E1 -f1 * (E1-E0)/(f1-f0)
        if np.abs(E2-E1) < tol : break
        E1,E0=E2,E1
    sol.append(E2)
        
print(sol)
   

