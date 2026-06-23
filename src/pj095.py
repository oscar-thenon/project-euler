from sympy.ntheory import divisor_sigma as ds
from math import inf
from src.fonctions import sigma_range

s = sigma_range(10**6,True)

chains = [0]*(10**6+1)
maxchain = 0
minmaxchain = 0

def sequence(n,last,sl,ss,l=1):
    global maxchain, minmaxchain
    ne = s[last]
    if (ne < n) or (ne > 10**6):
        for e in sl:
            chains[e] = inf
        return
    if ne in ss:
        if ne == n:
            for e in sl:
                chains[e] = l
            if l > maxchain:
                maxchain = l
                minmaxchain = min(sl)
        else:
            i = sl.index(ne)
            for j in range(i):
                chains[sl[j]] = inf
            lchain = l-i
            for j in range(i,l):
                chains[sl[j]] = lchain
            if lchain > maxchain:
                maxchain = lchain
                minmaxchain = min(sl[i:])
        return
    if chains[ne] != 0:
        for e in sl:
            chains[e] = inf
        return
    # All is ok, we adding the new element
    ss.add(ne)
    sequence(n,ne,sl+[ne],ss,l+1)
    return

for n in range(2, 10**6+1,1):
    if chains[n] == 0:
        sequence(n,n,[n],{n})

print("Answer is", minmaxchain)