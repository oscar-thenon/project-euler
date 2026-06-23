from math import log2

ks = [2*k for k in range(12001)] # We don't care about two first which are 0 and 1

def sequence(k,p=1,s=0,e=2,l=0):
    global ks
    if l == k:
        Nk = k+(p-s)
        if Nk <= 12000:
            eNk = ks[Nk]
            ks[Nk] = min(eNk,p)
        return
    else:
        p *= e
        while p <= 24000:
            s += e
            sequence(k,p,s,e,l+1)
            s -= e
            p //= e
            e += 1
            p *= e

for k in range(2,int(log2(24000))+1):
    sequence(k)
    
print("Answer is", sum(set(ks[2:])))