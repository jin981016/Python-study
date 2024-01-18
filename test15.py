import numpy as np
import matplotlib.pyplot as plt
"""
#bisection method

def fx(x):
    f= x**4 -3*x - 1
    return f

tol = 1.e-6
a,b=1,2
n=0
while True:
    c=0.5*(a+b)
    fc = fx(c)
    fa = fx(a)
    fb= fx(b)
    
    print(f'{n:1d} {a:.4f} {b:.4f} {abs(c-a):.4f} {fc:.4f}')
   
    if np.abs(c-a) < tol :
        solution = c
        break 
    if fa*fc < 0. :
        b = c
        n+= 1 
    else :
        a=c
        n+= 1 

print(solution)
"""

# False Position Method
def fx(x) :
    f= np.tan(np.pi * x) - 6
    return f
a,b=0. ,0.48
tol = 1.e-10
n=0
pfc = 0
fa=fx(a)
fb=fx(b)
while True :
    c=(a*fb-b*fa)/(fb-fa)
    fc=fx(c)
    print(f'n={n:1d} a={a:.5f} b={b:.5f} c={c:.5f}')
    if np.abs(c-a)< tol :
        soultion = c
        break
    if fa*fc <0 :
        b=c
        fb = fx(b)
        if fc*pfc > 0 :
            fa = 0.5*fa 
        n+=1 
    else :
        a=c
        fa = fx(a)
        if fc*pfc > 0 :
            fb = 0.5*fb
       
        n+=1
    pfc = fc 
print(fx(c),c)
        
