import time
start = time.time()

from math import sqrt

def decomp(nw,ln,r,lr,s):
    global iss
    if ln == 0:
        if s == r:
            iss = True
    elif ln >= lr:
        if int(nw[:lr]) <= r:
            for i in range(lr,0,-1):
                decomp(nw[i:],ln-i,r,lr,s+int(nw[:i]))
                if iss:
                    break
        else:
            for i in range(lr-1,0,-1):
                decomp(nw[i:],ln-i,r,lr,s+int(nw[:i]))
                if iss:
                    break
    else:
        for i in range(ln,0,-1):
                decomp(nw[i:],ln-i,r,lr,s+int(nw[:i]))
                if iss:
                    break
for k in range(2,10):
    start = time.time()
    ans = 0
    for r in range(4,int(sqrt(10**k))+1):
        s = r**2
        iss = False
        decomp(str(s),len(str(s)),r,len(str(r)),0)
        if iss:
            ans += s
    print(10**k,ans,round(time.time()-start,3))
            


