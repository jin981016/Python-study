import sys
import numpy as np
import matplotlib.pyplot as plt

a=0.
n=1000
for i in range(n) :
    a += 0.1
print(f'a={a:.14f} , err={a-n*0.1:.4e}')

exp = 1.0
while (1+exp) != 1 :
    exp0 = exp
    exp /= 2

print(exp0)


def fx(x) :
    y= x*(np.sqrt(x**2 +1) - x)
    return y
def tx(x) :
    y= x / (np.sqrt(x**2 +1) + x)
    return y
def gx(x):
    y= (1 - np.cos(x))/ x**2
    return y
def tgx(x) :
    y = 1/2 - x**2 / 24 + x**4 / 720
    u = (1/2)*(np.sin(x)/(x/2))**2
    return y,u
t =[1,10**2,10**4,10**6,10**8]
j= [1,10**(-2),10**(-4),10**(-6),10**(-8)]
for i in t :
    f = fx(i)
    print(f,"1")
for i in t :
    f = tx(i)
    print(f,"1")
for i in j :
    f = gx(i)
    print(f,"2")
for i in j :
    f = tgx(i)
    print(f,"2")
    

