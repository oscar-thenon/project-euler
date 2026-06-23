from math import sqrt
from sympy import gcd


def coprimes_with(n):
    """ Return a list of integers in [1,n[ which
    are coprimes with n and without the same parity """
    if (n%2 == 1):
        sieve = [[x,True] for x in range(2,n,2)]
        lsieve = (n-1)//2
        coprimes = []
        for (i,l) in enumerate(sieve):
            if l[1]:
                x = l[0]
                if gcd(x,n) == 1:
                    coprimes.append(x)
                else:
                    k = x//2
                    j = i+k
                    while j < lsieve:
                        sieve[j][1] = False
                        j += k
        return coprimes
    else:
        sieve = [[x,True] for x in range(1,n,2)]
        lsieve = (n//2)-1
        coprimes = []
        for (i,l) in enumerate(sieve):
            if l[1]:
                x = l[0]
                if gcd(x,n) == 1:
                    coprimes.append(x)
                else:
                    j = i+x
                    while j < lsieve:
                        sieve[j][1] = False
                        j += x
        return coprimes

N = 15*10**5
n = N//2
lim = int((-1+sqrt(1+4*n))/2)

# Generating primitive Pythagorean triples
triplets = []
for p in range(1,lim+1):
    p2 = p**2
    coprimes = coprimes_with(p)
    for q in coprimes:
        q2 = q**2
        t = [p2-q2,2*p*q,p2+q2]
        if sum(t) <= N:
            triplets.append(t)

# Occurrences of possible perimeters
occ = [0]*(n+1)

for t in triplets:
    s = sum(t)
    d = s
    while d <= N:
        occ[(d-2)//2] += 1
        d += s

print("Answer is", occ.count(1))