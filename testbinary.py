import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from mpl_toolkits.mplot3d import Axes3D

def acc(pos) :
    ac =np.zeros((pn,3))
    for i in range(pn):
        dpos= pos[i]-pos
        r=np.sqrt(np.sum(dpos**2,axis=1)+softn)
        r[i]=1
        g=-G*m[i]/(r**3)
        ac[i]=np.sum(g.reshape(pn,1)*dpos,axis=0)
    return ac


fig=plt.figure(1,figsize=(10,10))
ax=fig.add_subplot(111,projection='3d')

G=1e8
boxsize = np.array([1000,1000,1000])

pn= 2
softn=50
pos0 = nr.rand(pn,3)*boxsize


vmax = 100
v0 = (2*nr.rand(pn,3) - 1)*vmax

time = 10000

dt = 0.001
pos = np.zeros((time,pn,3))
massmax=2
m=nr.rand(pn,1)*massmax
posCM = np.zeros((time,1,3))
for i in range(time):
    pos[i] = pos0
    v0 += acc(pos0)*dt/2
    pos0 += v0*dt
    posCM[i] = (pos[i,0]*m[0] + pos[i,1]*m[1])/(m[0]+m[1])

for i in range(pn):
    ax.plot(pos[:,i,0],pos[:,i,1],pos[:,i,2],c='r',lw=1)
ax.plot(posCM[:,0,0],posCM[:,0,1],posCM[:,0,2],c='k',lw=1)



plt.show()
