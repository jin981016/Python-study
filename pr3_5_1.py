import numpy as np
import matplotlib.pyplot as plt
def FM(T,M) :
    y = (1-np.exp(-2*M/T))/((1+np.exp(-2*M/T))) 
    return y

def tanh(T,M) :
    y = np.tanh(M/T)
    return y
T=np.arange(2,0,-0.01)

tol=1.e-6

x=[]

for i in range(len(T)) :
    M=1.0
    a=T[i]
    while True:
        M1 =FM(a,M)
        if np.abs(M1-M) < tol : break
        M =M1
    x.append(M)



M=1.0
while True:
    M1 = FM(0.7,M)
    if abs(M1-M) < tol: break
    M =M1
print(M)


plt.plot(T,x)
plt.xlabel('T')
plt.ylabel('M')
plt.show()

