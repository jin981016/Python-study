import numpy as np
import matplotlib.pyplot as plt
def fx(a,b) :
    if a > b :
        quo = a//b
        rem = a%b
    else :
        quo = b//a
        rem = b%a
    return quo,rem
a=int(input('Input first interger : '))
b=int(input('Input second interger : '))
print('two intergers :',a,'and',b)
quo,rem = fx(a,b)
print('quoient',quo)
print('remainder',rem)
