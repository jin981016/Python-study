import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr

def logistic(r,x) :
    y = (r*x)*(1-x)
    return y

x=0.1

X=[]
Y=[]
counter={}
n=np.linspace(0,1000,1000)
t=10000
dr = 1/t
R=np.linspace(2.0,4.0,t)
for r in R:
    X.append(r)
    x=nr.random()            # (1)
    for i in range(1001):    # (2)
        x=logistic(r,x)
    for i in range(1001):   
        x=logistic(r,x)
    Y.append(x)
plt.plot(X,Y,ls='',marker=',')
plt.grid(True)
plt.minorticks_on()
plt.show()
"""
### dict에서 반복되는 값 찾아내는 코드.
for value in X:
    try: counter[value] += 1
    except: counter[value ] = 1


for key,value in counter.items() :
    if value >= 2 :
        print(key)


"""
