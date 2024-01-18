import numpy as np
import matplotlib.pyplot as plt


n=1234567
b=str('')
while n >=1 :
    r=n%2
    q=n//2
    if r ==0 :
        b += '0'
        n = q
    else :
        b += '1'
        n=q

c=str('')
for i in range(1,len(b)+1):
    c+=b[-i]
print(c,len(c))
n='1234567'
print(len(n))
