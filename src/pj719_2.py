import time
start = time.time()
from math import sqrt

COMB = dict()
COMBKEYS = {i for i in range(10)}

for i in range(10):
    COMB[i] = [i]
    
def decomp(n,r):
    """ Décompose n puis l'ajoute dans COMB
    et renvoie vrai si une des décomposition vaut
    la racine """
    global COMB
    iss = False
    w = str(n)
    l = len(w)
    new = {n}
    for i in range(1,l):
        prefix = int(w[:i])
        suffix = int(w[i:])
        if not(suffix in COMBKEYS):
            decomp(suffix,0)
        for s in COMB[suffix]:
            newsum = prefix+s
            if newsum == r:
                iss = True
            new.add(newsum)
    COMB[n] = list(new)
    COMBKEYS.add(n)
    return iss

ans = 0

for r in range(10**6+1,3,-1):
    s = r**2
    if decomp(s,r):
        ans += s
        
print("Answer is",ans)
print("\nExecution time :",round(time.time()-start,3))