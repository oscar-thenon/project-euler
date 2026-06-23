import time
start = time.time()

from math import *

def longueur(n):
    return int(log10(n)+1)

def decomp(nw,k,s):
    """nw : nombre à décomposer
    k : longueur restante
    r : la racine
    nr : la longueur de la racine
    s : la somme cumulée
    tab : la decomposition détaillée"""
    global r,nr,iss
    if k == 0:
        if s == r:
            iss = True
    else:
        for l in range(min(k,nr),0,-1):
            new = int(nw[:l])
            snew = s+new
            if (snew <= r):
                decomp(nw[l:],k-l,snew)
            if iss:
                break
            
answer = 0
for r in range(2,int(sqrt(10**4))+1):
    s = r**2
    iss = False
    nr = longueur(r)
    decomp(str(s),longueur(s),0)
    if iss:
        answer += s

print("Answer is",answer)
print("\nExecution time :",round(time.time()-start,3))