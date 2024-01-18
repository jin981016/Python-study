import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
"""
dat = np.loadtxt('data.txt')

e = dat[:,2]
r= dat[:,3]
plt.scatter(e,r)
plt.show()



"""
"""
G = 6.67e-11
R = 6400e3
M = 6e24
x0 ,y0 = 0,R
x,y= x0,y0
vx0,vy0 = 5000 , 0
vx , vy = vx0 , vy0
dt = 100
time = 1000
xls=[]
yls=[]

plt.scatter(0,0,s=100,c='b')
for i in range(time):
    r= x**2 + y**2
    g = -G*M/((r)**(3/2))
    vx += g*dt*x
    vy += g*dt*y
    x += vx*dt
    y += vy*dt
    xls.append(x)
    yls.append(y)

plt.plot(xls,yls,c='r',lw = 1)
plt.show()


a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
A = a[:,0]
B=a[:,1]
C=a[:,2]

print(A,B,C)

d = np.sum(a,axis=0)
print(d)
f = np.sum(a,axis=1)
print(f)
"""

boxsize = np.array([[500,1000]])
pn= 4
pos0 = nr.rand(pn,2)
M0 = np.array([[500,250]])
dpos = pos0 - M0
R = np.sqrt(np.sum(dpos**2,axis = 1))
print(pos0,R)
