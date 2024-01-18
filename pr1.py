import numpy as np
import matplotlib.pyplot as plt

a=str(input(''))
b=str('')
for i in range(len(a)) :
    if a[i].isupper() == True :
         b+= a[i].lower()
    
    else :
        b+=a[i].upper()

print(a)   
print(b)
    

