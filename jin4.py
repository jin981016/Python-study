import numpy  as np
import matplotlib.pyplot as plt

def test3(x,mylist):
    x += 2
    mylist.append(x)
    
a=3
b=[0]
print(a,b)
for i in range(a,10):
    test3(i,b)

print(b)

