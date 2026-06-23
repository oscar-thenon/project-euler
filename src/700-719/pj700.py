def bezout(a,d):
    """ Return (u,v) such as a*u+d*v = 1.
    a,d : integers such as a > d and gcd(a,d) = 1 """
    qs = []
    l = 0
    r = 0
    while r != 1:
        q = a//d
        qs.append(q)
        r = a-d*q
        a = d
        d = r
        l += 1
    if l == 1:
        return 1,-qs[0]
    elif l == 2:
        return -qs[1], 1+qs[0]*qs[1]
    else:
        u1, v1 = 1,-qs[0]
        u2, v2 = -qs[1], 1+qs[0]*qs[1]
        
        for k in range(2,l):
            u3, v3 = u1-u2*qs[k], v1-v2*qs[k]
            u1, v1 = u2, v2
            u2, v2 = u3, v3
        return u2,v2
    
    
def maj(eulercoins,l,r,n):
    i = -1
    while eulercoins[1][i] > n:
           eulercoins[1][i] = 0
           i -= 1
           while (i >= -l) and (eulercoins[1][i] == 0):
               i -= 1
           if i < -l:
               break
    eulercoins[0].append(r)
    eulercoins[1].append(n)

def solve(d,a,R,N):
    _,v = bezout(a,d)
    
    eulercoins = [[],[]]
    
    for r in range(R-1,-1,-1):
        
        k = (N-r*v)//a+1
        n = r*v+a*k
        if r == R-1:
            eulercoins[0].append(r)
            eulercoins[1].append(n)
            l = 1
        else:
            maj(eulercoins,l,r,n)
            l += 1
    ansaux2 = 0
    for (i,e) in enumerate(eulercoins[1]):
        if e != 0:
            ansaux2 += eulercoins[0][i]
    return ansaux2

d = 1504170715041707
a = 4503599627370517
R = 4349812 # The eulercoin from which we start solving
N = 7989455221 # The n corresponding to R

ansaux1 = 1517926496483919 # The sum of eulercoins above R
ansaux2 = solve(d,a,R,N) # The sum of eulercoins under R

print("Answer is", ansaux1+ansaux2)




""" dn = r [a]

<=> n = rv+ak and q = dk-ru"""
