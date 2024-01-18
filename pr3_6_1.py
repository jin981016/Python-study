import numpy as np

def sigma(m1,m2) :
    y= np.sqrt((m1+m2)/D**3)
    return y
def Grav(m,r1) :
    y = m / (np.linalg.norm(r-r1,ord=2))**3
    return y


m = 0.2


r1 =np.array([-m,0.])
r2 = np.array([(1-m),0.])
roots=[]
m1 = 4
m2 = 1
D = 1
tol = 1.e-6
for i in np.arange (-0.5,1,0.1) :
    r = np.array([i,0])

    while True :
        fx = Grav(m1,r1)*(r-r1) + Grav(m2,r2)*(r-r2) - sigma(m1,m2)**2 * r
        dfx = -2*(Grav(m1,r1) + Grav(m2,r2)) - sigma(m1,m2)**2
        err = fx/(dfx)
        errx = err[0]
        erry = err[1]
        if np.abs(errx) < tol : break
     
        r -= err

    roots.append([round(r[0],5),round(r[1],5)])


t= np.array(list(set([tuple(k) for k in roots])))
print(t)


roots=[]
for i in np.arange (-1,3,0.1) :
    r = np.array([i,i])

    while True :
        fx = Grav(m1,r1)*(r-r1) + Grav(m2,r2)*(r-r2) - sigma(m1,m2)**2 * r
        dfx = -2*(Grav(m1,r1) + Grav(m2,r2)) - sigma(m1,m2)**2
        err = fx/(dfx)
        errx = err[0]
        erry = err[1]
        if np.abs(erry) < tol : break
     
        r -= err

    roots.append([round(r[0],3),round(r[1],3)])



t= np.array(list(set([tuple(i) for i in roots])))
print(t)

        
