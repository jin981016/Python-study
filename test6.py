import matplotlib.pyplot as plt
import numpy as np

"""
x= np.linspace(0,2*np.pi,100)

y1=np.cos(x)
y2=np.sin(x)

plt.plot(x,y1,'r-',label='cosine')
plt.plot(x,y2,'b--',label='sine')
plt.xlim(0,2*np.pi)
plt.ylim(-1.3,1.3)
plt.xlabel('x value')
plt.ylabel('y value')
plt.title('example figure')
plt.axhline(y=0)
plt.axvline(x=np.pi)
plt.minorticks_on()
plt.legend()
"""

"""
fig=plt.figure(1,figsize=(10,5))
x=np.arange(1,6)
y1=x*x
y2=x**1.5
plt.subplot(2,2,1)
plt.plot(x,y1,'ro-')
plt.xlabel('x')
plt.ylabel('y')
plt.text(1,24,'(a)')
plt.minorticks_on()

plt.subplot(2,2,2)
plt.plot(x,y2,'bD--')
plt.xlabel('x')
plt.ylabel('y')
plt.text(1,10.6,'(b)')
plt.tight_layout()
plt.minorticks_on()
plt.savefig('figure.pdf')
plt.show()
"""
data1=np.random.normal(5.0,3.0,1000)
data2=np.random.normal(0.0,3.0,1000)
data3=np.random.normal(2.0,3.0,1000)
plt.hist(data1,bins=30,color='b',alpha=0.5,label='data1',density=True)
plt.hist(data2,bins=30,color='r',alpha=0.5,label='data2',density=True)
plt.hist(data3,bins=30,color='k',histtype='step',label='data3',hatch='/',density=True)

plt.ylabel('frequency')
plt.xlabel('data')
plt.legend()
plt.show()

