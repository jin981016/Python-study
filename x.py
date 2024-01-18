import math
import numpy as np
import matplotlib.pyplot as plt
def Binom(n,k):
  y = (math.factorial(n) /((math.factorial(k) * math.factorial(n-k))))*p**k *(1-p)**(n-k) 
  return y
N= 10
p = 0.3
summ =0



x=[]
y=[]
total=[]
for k in range(N+1) :
  t = Binom(N,k)
  x.append(k)
  y.append(t)
  summ += t
  total.append(summ)
fig = plt.figure(1,figsize = (10,5))

mu = N*p
sigma = (mu*(1-p))**0.5
t = np.random.normal(mu,sigma,N)
xbins = np.linspace(0.5,N+0.5,num=N+2)
plt.hist(t,xbins,cumulative = 1,density= True)


plt.show()

