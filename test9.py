import numpy as np
import matplotlib.pyplot as plt
import urllib.request
target='http://astro.snu.ac.kr/~wkim/PyData/bonnor.txt'
urllib.request.urlretrieve(target,'bonnor.txt')

fname='./bonnor.txt'
x,den,rds,pre = np.loadtxt(fname,unpack=True,usecols=[0,1,2,3])

fig = plt.figure(1,figsize=(10,5))
plt.subplot(121)
plt.xlim(0.1,100)
plt.ylim(1.e-3,2)
plt.loglog(x,den)
plt.text(40,1,r'$(a)$')
plt.ylabel(r'$\rho/\rho_0$')
plt.xlabel(r'$\xi$')
plt.subplot(122)
plt.xlim(0.2,1)
plt.ylim(0.,2)
plt.xticks(np.linspace(0.2,1.,5))
plt.yticks(np.linspace(0.,2.0,5))
plt.plot(rds,pre)
plt.grid(True)
plt.text(0.9,1.8,r'$(b)$')
plt.xlabel(r'$R$')
plt.ylabel(r'$P_{\rm ext}$')
plt.tight_layout()
plt.show()


"""
y=den*pre
f=open('output.txt','w')
for i in range(len(x)):
    txt=str(x[i])+'\t'+str(y[i])+'\n'
    f.write(txt)
    
f.close()

tmp=np.concatenate(([x],[y]),axis=0)
np.save('output',tmp)
z=np.load('output.npy')
x1=z[0,:]
y1=z[1,:]
print(x1==x)
print(y1==y)
"""
