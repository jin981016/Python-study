import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import linalg
import cmath
"""
def func(x):
    f=[x[0]*np.cos(x[1])-4+x[2],(x[0]-1)*x[1]-5+x[2],x[0]*x[1]*x[2]-10]
    return f

def Jacobi(x):
    J = [[np.cos(x[1]),-x[0]*np.sin(x[1]),1], [x[1],x[0]-1,1],[x[1]*x[2],x[0]*x[2],x[0]*x[1]]]
    return J

x=[5,0,5]
tol= 1.e-10

while True :
    J=Jacobi(x)
    f=func(x)

    Jinv=linalg.inv(J)
    err=np.dot(Jinv,f)
    if linalg.norm(err) < tol : break
    x= x-err
"""

"""
def func(x):
    f=[x[0]*np.cos(x[1])-4,(x[0]-1)*x[1]-5]
    return f
root=fsolve(func,[1,1],xtol=1.e-10)
print(root)
"""

def func(x) :
    f1 = np.abs(x[0]**2+ cmath.sqrt(1-x[1]) - 3+x[2])
    f2 = np.abs(np.log(x[0])+x[1]+2+x[2])
    f3 = np.abs(x[0]*x[1]*x[2]-5)
    return [f1,f2,f3]
root=fsolve(func,[2,2,2],xtol=1.e-10)
print(root)
