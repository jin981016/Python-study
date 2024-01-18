import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


fig= plt.figure(1,figsize=(10,5))
x=y=np.arange(-3,3.1,0.1)
X,Y=np.meshgrid(x,y)
z1 = np.exp(-X**2-Y**2)
z2= np.exp(-(X-1)**2-(Y-1)**2)
z=z1-z2

ax=plt.subplot(121)
im=ax.pcolormesh(x,y,z,cmap='bwr')
plt.xlabel('x')
plt.ylabel('y')
ax.set_aspect(aspect=1)
divider = make_axes_locatable(ax)
cax=divider.append_axes("right",size=0.2,pad=0.1)
cbar=plt.colorbar(im,cax=cax)
cbar.set_label(r'$\delta\rho$')

ax=plt.subplot(122)
im=plt.imshow(z,cmap='RdBu',origin='lower',extent=[-3,3,-3,3])
plt.xlabel('x')
plt.ylabel('y')
divider = make_axes_locatable(ax)
cax=divider.append_axes("top",size=0.2,pad=0.1)
cbar=plt.colorbar(im,cax=cax,orientation='horizontal')
cbar.ax.xaxis.set_ticks_position("top")
cbar.ax.set_title(r'$\delta\rho$',y=3.5)
plt.tight_layout()
plt.show()

"""
theta = np.linspace(0,2*np.pi,100)
r=np.linspace(0,10,200)
R,Theta = np.meshgrid(r,theta)
data = np.sin(2*Theta)*np.cos(R)
plt.subplot(projection="polar")
plt.pcolormesh(theta,r,data.T)
plt.show()
"""
