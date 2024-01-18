import numpy as np
import matplotlib.pyplot as plt
import sys

def Kahan(x):
    c,summ = 0,0
    for i in range(len(x)):
        xp=x[i] - c
        sp =summ
        summ += xp
        c = ((sp+xp)-sp) - xp
        print(c)

    return summ

def Directsum(x) :
    summ=0
    for i in range(len(x)) :
        summ += x[i]
    return summ
num = 10
n=np.logspace(1,5,num).astype(int)
kerr=np.zeros(num)
derr = np.zeros(num)
perr = np.zeros(num)

for i in range(num) :
    x=np.ones(n[i])*0.1
    trueval = (n[i]*0.1)
    kerr[i] = np.abs(Kahan(x)-trueval)
    derr[i] = np.abs(Directsum(x)-trueval)
    perr[i] = np.abs(np.sum(x) - trueval)

fig =plt.figure(1,figsize=(10,5))
plt.subplot(121)
plt.plot(n,derr,'--',label='Directsum')
plt.plot(n,perr,':',label = 'np.sum()')
plt.plot(n,kerr,'-',label = 'Kahan sum')
plt.xscale('log')
plt.xlabel('n')
plt.ylabel('error')
plt.legend()

plt.subplot(122)
plt.plot(n,derr,'s',label='Direct sum')
plt.plot(n,perr,'o',mfc='w',mec='k',label='np.sum()')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('error')
plt.legend(numpoints=3)
plt.tight_layout()
plt.show()
