import numpy as np

def func(x) :
    y= np.sin(x)
    return y

def Midpoint(F,a,b,n) :
    h= (b-a) / float(n)
    summ = 0
    for j in range(n) :
        c= a+(j+0.5)*h
        summ += F(c)
        
    return summ*h


a,b=0,np.pi

perr = 1

for i in range(0,10) :
    n = 2**i
    h= (b-a) / float(n)
    sol = Midpoint(func,a,b,n)
    err = abs(2.-sol)
    ratio = perr/err
    perr = err
   # corr = abs(sol - (((b-a)*h**2)/24)*(func(b)-func(a)) - 2.0)
    print(f'{n:3d} {sol:.6f} {err:.4e} {ratio:.2f} ')
