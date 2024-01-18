import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr

"""
#newton method 
def NR(x) :
    f = x**4 -3*x - 1
    df = 4*x**3 - 3
    return f, df

x,tol=2.0 , 1.e-6
n=0
while True :
    n+=1
    f0,df = NR(x)
    ratio = f0/df
    print(f' n={n} x={x:.4f} f0={f0:.4f} df = {df:.4f}')
    if np.abs(ratio) < tol :
        break
    x -= ratio
    
print(x,ratio)
"""

def fx(x) :
    y= x**4-3*x -1
    return y

x0,x1=1,2
tol = 1.e-6

n=0
while True:
    n+=1 
    f0 =fx(x0)
    f1= fx(x1)
    x2 = x1 - f1*(x1-x0)/(f1-f0)
    f2= fx(x2)
    print(f'n={n} x2={x2:.4f} f2={f2:.4f} |x2-x1|={np.abs(x2-x1):.5e}')
    if np.abs(x2-x1) < tol :
        
        break
    x0 = x1
    x1 = x2
print(x2)
