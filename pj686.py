from math import *

def bound(p):
    return (log10(123)+p)/log10(2)

D = (log10(124)-log10(123))/log10(2)

p = 0
b = bound(p)

n = 678910

for i in range(n):
   
    while ceil(b)-b > D:
        p += 1
        b = bound(p)
    
    if (i == n-1):
        print("Answer is", ceil(b))
    
    p += 58
    b = bound(p)