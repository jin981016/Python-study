import numpy as np
import matplotlib.pyplot as plt

def der(a,b,c) :
    x1 = (-b+np.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-np.sqrt(b*b-4*a*c))/(2*a) 
    return x1,x2

a,b,c=1,2,1
x1,x2=der(a,b,c)
if x1==x2 :
    print(x1,'(중근)')
else:
    print(x1,x2)
