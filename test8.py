import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

x=y=np.arange(-3,3.1,0.1)
X,Y=np.meshgrid(x,y)
z1=np.exp(-X**2-Y**2)
z2=np.exp(-(X-1)**2-(Y-1)**2)
z=z1-z2

fig=plt.figure(1,figsize=(5,5))
plt.contourf(X,Y,z,cmap='jet_r')
lev=[-0.6,-0.3,0,0.3,0.6]
cs=plt.contour(X,Y,z,levels=lev,colors='k')
plt.clabel(cs)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
