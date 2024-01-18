import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from mpl_toolkits.axes_grid1 import make_axes_locatable

#x=nr.random()


r=np.arange(2.0,4.0,10**(-2))
xl=np.arange(1000,1100,0.5)
t=[]


for j in range(len(r)):
    x=[0.1]
    for i in np.arange(0,1101,1):
        y=r[j]*x[i]*(1-x[i])
        x.append(y)
    g=x[1000:1100]
    t.append(g)

plt.xticks(np.linspace(2.0,4.0,5))
plt.yticks(np.linspace(0.0,1.0,5))
plt.grid(True)
plt.minorticks_on()
plt.plot(r,t,'k')

    

plt.show()
       

