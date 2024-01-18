import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from mpl_toolkits.mplot3d import Axes3D

G=1e8
m1=5
m2=5

M=(m1*m2)/(m1+m2)

boxsize = np.array([1000,1000])

pos01 =(nr.rand(1,2))*boxsize
pos02=(nr.rand(1,2))*boxsize


vmax = 100
v01 = (2*nr.rand(1,2) - 1)*vmax
v02 = (2*nr.rand(1,2) - 1)*vmax

time = 100

dt = 0.011


pos1 = np.zeros((time,1,2))
pos2 = np.zeros((time,1,2))


for i in range(time):
    posCM = (m1*pos01 +m2*pos02)/(m1+m2)
    plt.scatter(posCM[:,0],posCM[:,1],c='k',s=1)
    dpos1 = pos01 - posCM
    dpos2 = pos02 - posCM
    r1 = np.linalg.norm(dpos1,ord=2)
    r2 = np.linalg.norm(dpos1,ord=2)
    g1= -G*m2 / (r1**3)
    g2= -G*m1 / (r2**3)

    a1= g1*dpos1
    a2= g2*dpos2
    v01 += a1*dt/2
    v02 += a2*dt/2
    pos01 += v01*dt
    pos02 += v02*dt
    pos1[i] = pos01
    pos2[i] = pos02
    
plt.plot(pos1[:,0,0],pos1[:,0,1],c='r',lw=1)
plt.plot(pos2[:,0,0],pos2[:,0,1],c='r',lw=1)


plt.scatter(pos1[-1,0,0],pos1[-1,0,1],c='b',s=50)
plt.scatter(pos2[-1,0,0],pos2[-1,0,1],c='b',s=50)
plt.xlim(-boxsize[0],boxsize[0])
plt.ylim(-boxsize[1],boxsize[1])



plt.show()
