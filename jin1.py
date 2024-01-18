import numpy as np
import matplotlib.pyplot as plt
"""
a='12.541 12.555 12.323 12.554 12.366 999 999    999'

a= a.split(' ')
print(a)
s=0
a=list(map(float,a))
b = 99
for i in range(len(a)):
    if float(a[i]) > 99  :
        continue
    else:
        s+= float(a[i])

f = open('data.txt','r')
dat =f.read()
dat = dat.split('\n')
x=[]
y=[]
for i in range(1,len(dat)-1) :
    line = dat[i].split()
    print(line)
    x.append(float(line[2]))
    y.append(float(line[3]))
    
plt.scatter(x,y)
plt.show()
"""
h= 6.626*10**(-34)
c = 3*10**8
k=1.38*10**(-23)
def Planck(x,T) :
    y = (2 * h * c**2) / ((np.exp(h*c/(x*k*T))-1)*x**5)
    return y


tx=[]
ty=[]
for j in range(1000,10001,1000):
    t= j
    x=[]
    y=[]
    n=10
    for i in np.arange(0.0001,5000,n) :
        l = i*10**(-9)
        intesity = Planck(l,t)
        x.append(intesity)
        y.append(i)
    a= max(x)
    lt = x.index(a)
    plt.scatter(lt*n,a)
    plt.plot(y,x,label ="T= {0}".format(t))
    ty.append(a)
    tx.append(lt*n)
    if x == 10**13 :
        plt.scatter(y[i],x[i])
        print(y)
    plt.legend()
plt.plot(tx,ty)

plt.xlim(0,2000)
plt.show()
