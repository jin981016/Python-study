import numpy as np
import matplotlib.pyplot as plt
"""
def test4(a,*args,**kwards) :
    print(a)
    print(args)
    print(kwards)
    for arg in args :
        print('an element in args = ',arg)
    for key , value in kwards.items() :
        print(f'key={key},value={value}')

test4(2,5,7,'a', 3,alpha = 3, gamma = 5,g=5)
"""

f= lambda x: x**2
print(f(5))

mini = lambda x,y : x if x<y else y
print(mini(13,12))

Celsius=[0,10,20,30]
Fahrenheit = map(lambda x :(9/5.)*x +32,Celsius)
list(Fahrenheit)


