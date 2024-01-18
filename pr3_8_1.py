import numpy as np
from scipy import linalg

def func(x):
    f= [(2*x[0]+x[1]-x[0]*x[1]+5) ,(2*x[0]*np.exp(-x[1]) - 1) ]
    return f

def Jaco(x) :
    J=[[2-x[1],1-x[0]],[2*np.exp(-x[1]),(-2)*x[0]*np.exp(-x[1])]]
    return(J)

x=[-5,-5]


tol = 1.e-10
xroots=[]
yroots=[]
roots=[]
for i in range (1,10) :
    x = [i,i]
    while True :
        
        J= Jaco(x)
        f = func(x)
        Jinv= linalg.inv(J)
        err =np.dot(Jinv,f)
        if linalg.norm(err) < tol : break
        x-=err
    xroots.append(round(x[0],6))
    roots.append([round(x[0],6),round(x[1],6)])

t= np.array(list(set([tuple(i) for i in roots])))
print(t)
