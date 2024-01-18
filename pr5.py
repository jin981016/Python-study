import numpy as np
import matplotlib.pyplot as plt

nmax=10**(4)

n=np.arange(1,nmax+1,1)
for i in range(len(n)):
    summ=0
    sumnol=0
    for j in range(1,len(n)+1):
        t=n[i]%j
        if t == 0:
            summ += 1
    if summ == 2 :
        sumnol += 1

print(sumnol)
    
