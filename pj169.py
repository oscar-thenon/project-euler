from math import *
from itertools import product
from baseconvert import *

N = 11

def b2(n):
    return base(n,10,2,string=True)

b = '110110'
a = '1010'

def tab(a,b):
    la = len(a)
    lb = len(b)
    if la >= lb:
        t = [0 for i in range(la)]
        for i in range(1,lb+1):
            t[i-1] += (a[-i] == '1')
            t[i-1] += (b[-i] == '1')
        for i in range(lb+1,la+1):
            t[i-1] += (a[-i] == '1')
    else:
        t = [0 for i in range(lb)]
        for i in range(1,la+1):
            t[i-1] += (a[-i] == '1')
            t[i-1] += (b[-i] == '1')
        for i in range(la+1,lb+1):
            t[i-1] += (b[-i] == '1')
            
    return(tuple(t))

    
file = open("pj169_donnees.txt","w")

for k in range(1,2**N):
    s = set()
    c = 0
    for a in range(1,k//2+1):
        b = k-a
        ba = b2(a)
        bb = b2(b)
        t = tab(ba,bb)
        if not t in s:
            s.add(t)
            c += 1
    file.write(str(k)+","+b2(k)+","+str(c)+"\n")
            
file.close()
            
        
        
        
        


