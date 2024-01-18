import numpy as np

m_e = 9.109e-31
eV = 1.602e-19
xion = 13.6 * eV
h=6.626e-34
k = 1.381e-23
gplus = 1
gzero = 2

n_H = 1e4*1e6
n_e = n_H *(0.5)
a=((2*gplus) /(gzero*n_e))*((2*np.pi*m_e*k)/h**2)**(3/2)

b = xion/ k


tol=1.e-6

x = 1e6

while True :
    fx = a*x**(3/2)*np.exp(-b/x) - 1.0
   
    dfx =a*x**(-1/2)*np.exp(-b/x)*((3/2)*x +b)

    err = (fx)/(dfx)

    if np.abs(err) < tol : break
    x -= err

print(x)

