import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import numpy.random as nr

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(111,projection='3d')

pn = 10
boxsize = np.array([1000,500,500])
pos0 = nr.rand(pn,3) * boxsize
Vmax = 150
V0 = (2*nr.rand(pn,3) - 1)*Vmax
M0 = np.array([400,230,230])

G = 1e8
M= 1
dt = 0.01
time = 1000
ax.scatter(pos0[:,0],pos0[:,1],pos0[:,2],c='b',s=5)

dat = np.zeros([time,pn,3])
for i in range(time) :
    dpos = pos0 -M0
    R = np.sum(dpos**2,axis=1) **(1/2)
    g = -G*M/(R**3)
    g = g.reshape(pn,1)
    Acc = g*dpos
    V0 += Acc*dt / 2
    pos0 += V0*dt
    dat[i] =pos0
        
for i in range(pn):
    ax.plot(dat[:,i,0],dat[:,i,1],dat[:,i,2],lw=1)
ax.scatter(pos0[:,0],pos0[:,1],pos0[:,2],c='g')

ax.scatter(M0[0],M0[1],M0[2],c='b',s=100)


ax.set_xlim(0,boxsize[0])
ax.set_ylim(0,boxsize[1])
ax.set_zlim(0,boxsize[2])

plt.show()

