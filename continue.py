import numpy as np

a='12.541 12.555 12.323 12.554 12.366 999 999 999'

a= a.split(' ')
print(a)
s=0
a=list(map(float,a))
b = 99
for i in range(len(a)):
    if float(a[i]) > 99  :
        continue
    else:
        s+= float(a[i])

print(s)            


f= open('FeI.arc.lin','r')

dat=f.read()
print(dat)
